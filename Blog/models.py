from distutils.command.upload import upload
from email.policy import default
from turtle import title
from unicodedata import name
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    picture = models.ImageField(default=True, upload_to="image/")
    
    def __str__(self):
        return self.title
