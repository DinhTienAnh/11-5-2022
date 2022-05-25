from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from  phonenumber_field.formfields import PhoneNumberField
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = '__all__'
        exclude = ['user']

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'bio', 'avatar', 'name','phoneNumber']
        
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'bio', 'avatar','name', 'password1' , 'password2', 'phoneNumber']
    
            
