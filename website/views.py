from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    
    return render(request, 'home.html', {})


def login(request):
    pass


def logout(request):
    pass