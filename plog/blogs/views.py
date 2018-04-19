from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html')

def view_blog(request, blog_id):
    return render(request, 'blogs/view.html')
