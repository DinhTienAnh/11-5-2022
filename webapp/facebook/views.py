from re import U
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import redirect, render
from facebook.models import Post,CustomUser, Comment
from django.contrib import messages
from . import forms

def login(request):
    if request.user.is_authenticated:
        return redirect('facebook:profile', pk = request.user.id)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            auth_login(request,user)
            return redirect('facebook:profile', pk = user.id)
        else:
            pass 
    context = {}
    return render(request, template_name='facebook/login.html', context=context)

def homePage(request,pk):
    form = forms.PostForm()
    user = CustomUser.objects.get(id = pk)
    posts = user.post_set.all().order_by('-created_at')
    if request.method == 'POST':
        post = request.POST.get('post')
        image = request.POST.get('image')
        Post.objects.create(
            user = request.user, 
            post = post, 
            images = image)
        return redirect('facebook:home-page',pk = user.id)
    context = {'user':user, 'posts':posts, 'form':form}
    return render(request, 'facebook/homepage.html', context=context) 


def profile(request, pk):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userLogin = authenticate(request, username = username, password = password)
        if userLogin is not None:
            auth_login(request,userLogin)
            return redirect('facebook:profile', pk = userLogin.id)
        else:
            pass 
    user = CustomUser.objects.get(id = pk)
    posts = user.post_set.all().order_by('-created_at')
    context = {'user':user, 'posts':posts}
    return render(request, 'facebook/profile.html',context)


def register(request):
    form = forms.MyUserCreationForm()
    if request.method == 'POST':
        form = forms.MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            auth_login(request,user)
            return redirect('facebook:profile', pk = user.id)
    context = {'form':form}
    return render(request, 'facebook/register.html',context)

def test(request):
    return render(request, 'facebook/login.html')



def logoutUser(request):
    logout(request)
    return redirect('facebook:login')