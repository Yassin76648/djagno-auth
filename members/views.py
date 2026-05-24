from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, "Wrong Credentials, Try Again...")
            return redirect("login")
    else:
        return render(request, "members/login.html")


def home(request):
    return render(request, 'members/home.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out...")
    return redirect('home')