from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request): # ruf die seite # wenn ich zu page gehe : GET., wenn ich in page login mache : POST wie senden data. 
    records = Record.objects.all()
    
    
    # check to see if login
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate To Login # sichern
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('home')
        else:
            messages.success(request, 'Please try again!')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request,'You are logged out!')
    return redirect('home')


def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate, Login
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have successfully Registered! We come!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You Must Be Logged In To View That Page..')
        return redirect('home')



def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, '"Record Deleted Successfully...')
        return redirect('home')
    else:
        messages.success(request, 'You Must Be Logged In To Delete..')
        return redirect('home')


def add_record(request):
    return render(request, 'add_record.html', {})
