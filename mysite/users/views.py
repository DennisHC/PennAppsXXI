from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {"form": form})

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')