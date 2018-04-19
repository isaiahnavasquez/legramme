from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

# for viewing blog
def view_blog(request, blog_id):
    return render(request, 'blogs/view.html')

# for viewing user profile
def view_profile(request, user_id):
    return render(request, 'blogs/profile.html')
