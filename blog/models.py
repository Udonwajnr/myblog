
from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
# Create your models here.

class User(AbstractUser):
    # pass
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField( null=True, upload_to='blog_media', default="images/avatar.svg")
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name    
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category , related_name='category')
    title = models.CharField(max_length=200, blank=False,unique=True);
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_media') 
    url = models.URLField(null=True, blank=True)
    body = HTMLField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} {self.message}"
    
class Contact(models.Model):
    name = models.CharField(max_length=200 , unique=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.email