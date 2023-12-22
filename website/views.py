from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request): # ruf die seite # wenn ich zu page gehe : GET., wenn ich in page login mache : POST wie senden data. 
    # check to see if login
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate To Login # sichern
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You You are logged in!")
            return redirect('home')
        else:
            messages.success(request, 'Please try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request,'You are logged out!')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})