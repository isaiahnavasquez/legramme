from django.urls import path

from . import views
app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.view_blog, name='view'),
    path('user/<str:user_id>/', views.view_profile, name='profile'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]
