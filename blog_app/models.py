from django.db import models
from django.contrib.auth.models import AbstractUser
class User(models.Model):
    username = models.CharField(max_length=120,unique=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120, null=True)

class Blog(models.Model):
    username = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=120, null=True)
    blog = models.CharField(max_length=2000, null=True)
    blog_id = models.IntegerField(unique=True, null=True)
# Create your models here.
