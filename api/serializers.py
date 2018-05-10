from rest_framework import serializers
from blogs.models import Blog, Category, Hashtag, Profile
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'pub_date', 'category', 'author', 'cover_photo', 'user')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        
class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    blogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'blogs')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    
    class Meta:
        model = Profile
        fields = ('user', 'default_pic', 'about')
