from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

from .models import Category, Blog, Profile

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
        return render(request, 'blogs/register.html')
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        profile = Profile(user=user, about=request.POST['about'])
        user.first_name = request.POST['name']
        user.save()
        profile.save()
        login(request, user)
        return render(request, 'blogs/home.html', {
            'message': 'Thanks for joining, %s' % user.first_name
        })

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
    return render(request, 'blogs/index.html', {
        'blogs': blogs,
        'users': users,
    })

def post_blog(request):
    user = request.user
    title = request.POST['title']
    body = request.POST['blog_body']
    category = get_object_or_404(Category, name=request.POST['category'])
    blog = Blog(title=title, content=body, category=category, author=user, pub_date=timezone.now())
    # import pdb; pdb.set_trace()
    if 'cover_photo' in request.FILES:
        cover_photo = request.FILES['cover_photo']
        fs = FileSystemStorage()
        filename = fs.save(cover_photo.name, cover_photo)
        blog.cover_photo = cover_photo
    blog.save()
    return HttpResponseRedirect(reverse('blogs:view_blog', args=(user.username,blog.id)))

def view_blog(request, user_name, blog_id):
    user_info = get_object_or_404(User, username=user_name)
    blogs = Blog.objects.filter(author=user_info)
    return render(request, 'blogs/view.html', {
        'blog_info': get_object_or_404(Blog, pk=blog_id),
        'author': user_name,
        'blogs': blogs,
        'about': get_object_or_404(Profile, user=user_info).about,
    })
