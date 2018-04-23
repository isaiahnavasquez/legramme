from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_pic = models.ImageField(upload_to='images/profiles/', default='images/default/empty-profile.png')
    about = models.CharField(max_length=100)

    def __str__(self):
        return self.about

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='images/blog_covers/', default='images/default/cover_default.jpg')

    def __str__(self):
        return self.title

class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    blog = models.ManyToManyField(Blog)

    def __str__(self):
        return self.name
