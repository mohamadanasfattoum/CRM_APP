from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check to see if login
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Yuo Have been Logged In!')
            return redirect('home')

        else:
            messages.success(request,'Plaese Try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    pass