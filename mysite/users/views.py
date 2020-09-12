from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {"form": form})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        username = username.cleaned_data

        password = request.POST.get('password')
        password = password.cleaned_data

        user = authenticate(username = username, password = password)
        if user is not None:
            print("You did it!")
            login(request, user)
            return redirect('homepage')
        else:
            print("Login failed")
            return redirect('login')
    else:
        context = {}
        return render(request, 'users/login.html', context)

def logout(request):
    return render(request, 'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')