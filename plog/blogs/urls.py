from django.urls import path

from . import views
app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.view_blog, name='view'),
    path('<str:user_id>/', views.view_profile, name='profile')
]
