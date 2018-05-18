from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.core import serializers

from .models import Category, Blog, Profile, Hashtag
from .forms import UserForm

# Create your views here.
blogs = Blog.objects.all()
users = User.objects.all()

def index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'blogs/index.html', {
            'about_text': profile.about,
            'blogs': blogs,
            'users': users,
        })
    else:
        return render(request, 'blogs/index.html', {
            'blogs': blogs,
            'users': users,
        })

# for viewing blog
def view_blog(request, blog_id):
    return render(request, 'blogs/view.html')

def hashtag(request, hashtag_name):
    hashtag = Hashtag.objects.get(name=hashtag_name)
    blogs = hashtag.blog.all()

    return render(request, 'blogs/hashtag.html', {
        'blogs': blogs,
        'hashtag_name': hashtag_name
    })

# for viewing user profile
def view_profile(request, user_name):
    user_info = get_object_or_404(User, username=user_name)
    blogs = Blog.objects.filter(author=user_info)
    about = Profile.objects.get(user=user_info)
    return render(request, 'blogs/profile.html', {
        'user_info': user_info,
        'blogs': blogs,
        'about': about.about,
    })

def upload_profile_photo(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if 'profile_photo' in request.FILES:
        profile_photo = request.FILES['profile_photo']
        fs = FileSystemStorage()
        fs.save(profile_photo.name, profile_photo)
        profile.default_pic = profile_photo
        profile.save()
    return HttpResponseRedirect(reverse('blogs:profile', args=(user.username,)))

# log in
def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'blogs/home.html')
        else:
            return render(request, 'blogs/login.html')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # import pdb; pdb.set_trace()
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('blogs:index'))
        else:
            return render(request, 'blogs/login.html', {
                'error_message': 'Invalid Credentials. Please Try Again.'
            })

# register an account
def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'blogs/register.html', {'form': form})
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            # check for password mismatch
            if request.POST['password'] == request.POST['confirm_password']:
                # check for username duplicates
                if User.objects.filter(username=request.POST['username']).count() == 0:
                    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                    profile = Profile(user=user, about=request.POST['about'])
                    user.first_name = request.POST['name']
                    user.save()
                    profile.save()
                    login(request, user)
                    return render(request, 'blogs/home.html', {
                        'message': 'Thanks for joining, %s' % user.first_name
                    })
                else:
                    return render(request, 'blogs/register.html', { 'form': form, 'error_message': 'Username already exists' })
            else:
                return render(request, 'blogs/register.html', { 'form': form, 'error_message': 'Passwords do not match' })
        else:
            return render(request, 'blogs/register.html', { 'form': form })


# gets the account profile for adding/editing blogs
def home(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(author=request.user)
        return render(request, 'blogs/home.html', {
            'blogs': blogs
        })
    else:
        return render(request, 'blogs/login.html', {'error_message': 'Please Log in to continue'})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))
    # return render(request, 'blogs/index.html', {
    #     'blogs': blogs,
    #     'users': users,
    # })

def post_blog(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'blogs/login.html', {'error_message': 'Please log in first to post a blog'})
        else:
            return render(request, 'blogs/home.html')
    else:
        user = request.user
        title = request.POST['title']
        body = request.POST['blog_body']
        category = get_object_or_404(Category, name=request.POST['category'])
        blog = Blog(title=title, content=body, category=category, author=user, pub_date=timezone.now())

        # save cover image
        if 'cover_photo' in request.FILES:
            cover_photo = request.FILES['cover_photo']
            fs = FileSystemStorage()
            filename = fs.save(cover_photo.name, cover_photo)
            blog.cover_photo = cover_photo

            # save hashtags
            blog.save()
            tags = [i for i in body.split() if i[0] == '#']
            for tag in tags:
                print(tags)
                print(blog)
                if Hashtag.objects.filter(name=tag[1:]).count() == 0:
                    hashtag = Hashtag(name=tag[1:])
                    hashtag.save()
                else:
                    hashtag = Hashtag.objects.get(name=tag[1:])

                    hashtag.blog.add(blog)

                    return HttpResponseRedirect(reverse('blogs:view_blog', args=(user.username,blog.id)))


def view_blog(request, user_name, blog_id):
    user_info = get_object_or_404(User, username=user_name)
    blogs = Blog.objects.filter(author=user_info)
    return render(request, 'blogs/view.html', {
        'blog_info': get_object_or_404(Blog, pk=blog_id),
        'author': user_name,
        'blogs': blogs,
        'user': user_info,
        'about': get_object_or_404(Profile, user=user_info).about,
    })

def search_site(request):
    text = request.GET['search_text']
    data = {
        'blogs_title': [],
        'tags_name': [],
        'users_username': [],
    }

    if len(text) > 0:
        # result: blogs:title
        blogs_title = Blog.objects.filter(title__startswith=text)
        # result: blogs:category
        blogs_category = Category.objects.filter(name__startswith=text)
        # result: tags:name
        tags_name = Hashtag.objects.filter(name__startswith=text)
        # result: users:username
        users_username = User.objects.filter(username__startswith=text)

        data = {
            'blogs_title': [{
                'title': i.title,
                'author': i.author.username,
                'id': i.id
            } for i in blogs_title],
            'tags_name': [{
                'name': i.name
            } for i in tags_name],
            'users_username': [{
                'username': i.username
            } for i in users_username]
        }

    return JsonResponse(data)
