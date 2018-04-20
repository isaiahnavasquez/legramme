from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
