from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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

# log in template

def login(request):
    if request.method == 'POST':
        return render(request, 'blogs/login.html')
    else:
        user = User.objects.create_user(request.POST['username'], '', request.POST['password'])
        user.save()
        return HttpResponseRedirect(reverse('blogs:home'))

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'blogs/home.html')
    else:
        return render(request, 'blogs/login.html', {'error_message': 'Please Log in to continue'})
