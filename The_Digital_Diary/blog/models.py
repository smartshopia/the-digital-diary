from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django_ckeditor_5.fields import RichTextField


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    contenttinMCE = HTMLField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Post1(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]