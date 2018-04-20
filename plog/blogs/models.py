from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_text = models.CharField(max_length=500)

class Category(models.Model):
    category_text = models.CharField(max_length=50)
