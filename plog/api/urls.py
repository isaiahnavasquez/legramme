from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
app_name = 'api'

urlpatterns = [
    path('blogs', views.blog_list, name="blog_list"),
    path('blogs/<int:pk>', views.blog_details, name="blog_details"),
]
