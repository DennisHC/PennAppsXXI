from django.shortcuts import render, redirect
from django.http import HttpResponse

def about(request):
    return render(request, 'info/about.html')

def facts(request):
    return render(request, 'info/facts.html')