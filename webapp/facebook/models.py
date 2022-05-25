from distutils.command.upload import upload
from email.policy import default
from enum import unique
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from webapp.settings import MEDIA_ROOT
# Model User
class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True) 
    email = models.EmailField(null=False, unique=True)
    bio = models.CharField(max_length=264, null=True)
    avatar = models.ImageField(default = None, upload_to = 'facebook/images/user/avatar/%Y/%m')
    wall = models.ImageField(default = None, upload_to = 'facebook/images/user/wall/%Y/%m')
    address = models.TextField(max_length=264, null=True)
    DoB = models.DateField(max_length=8, null=True)
    phoneNumber = PhoneNumberField(blank = True, unique = False, default = None)
    website = models.CharField(max_length=64,null=True)
    
    def __str__(self):
        return self.username
    
    
    
class Post(models.Model):
    post = models.TextField(max_length=264, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    images = models.ImageField(default = None, upload_to = 'facebook/images/post/%Y/%m')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.post[0:50]
    
class Comment(models.Model):
    body = models.TextField(max_length=264)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[0:50]

class Like(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like_status = models.BooleanField(default=False)

class Share(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    share_status = models.BooleanField(default=False)

