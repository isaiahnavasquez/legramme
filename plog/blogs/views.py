from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

# for viewing blog
def view_blog(request, blog_id):
    return render(request, 'blogs/view.html')

# for viewing user profile
def view_profile(request, user_id):
    return render(request, 'blogs/profile.html')

# log in
def login(request):
    template_name = 'blogs/home.html'
    if request.method == 'GET':
        return render(request, template_name)
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            return render(request, template_name)
        else:
            return render(request, template_name, {
                'error_message': 'Invalid Credentials. Please Try Again.'
            })

# register an account
def register(request):
    if request.method == 'GET':
        return render(request, 'blogs/register.html')
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        return render(request, 'blogs/home.html', {
            'message': 'Thanks for joining, %s' % user.first_name
        })


# gets the account profile for adding/editing blogs
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'blogs/home.html')
    else:
        return render(request, 'blogs/login.html', {'error_message': 'Please Log in to continue'})
