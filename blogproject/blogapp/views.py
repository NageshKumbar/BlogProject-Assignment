# blogapp/views.py
from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


@login_required(login_url='login')
def create_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        Blog.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('home')

    return render(request, 'create.html')


def user_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')