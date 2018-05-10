from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('blogs/', views.BlogList.as_view()),
    path('blogs/<int:pk>', views.BlogDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('profile/<int:pk>', views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
