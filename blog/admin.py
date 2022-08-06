from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Category, Post,User,Comment,Contact
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
