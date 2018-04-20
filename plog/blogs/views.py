from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
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
def login_user(request):
    if request.method == 'GET':
        return render(request, 'blogs/login.html')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # import pdb; pdb.set_trace()
        if user is not None:
            login(request, user)
            return render(request, 'blogs/home.html')
        else:
            return render(request, 'blogs/login.html', {
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
        login(request, user)
        return render(request, 'blogs/home.html', {
            'message': 'Thanks for joining, %s' % user.first_name
        })

# gets the account profile for adding/editing blogs
def home(request):
    if not request.user.is_authenticated:
        return render(request, 'blogs/home.html')
    else:
        return render(request, 'blogs/login.html', {'error_message': 'Please Log in to continue'})

def logout_user(request):
    logout(request)
    return render(request, 'blogs/index.html')
