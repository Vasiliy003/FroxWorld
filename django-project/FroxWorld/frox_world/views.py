from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login

from .models import *
# Create your views here.
def index(request):
    servers = Server.objects.all()
    context = {
        "servers": servers,
        "title": "FroxWorld"
        }

    return render(request, 'index.html', context)

def donate(request):
    servers = Server.objects.all()
    privilegeTypes = PrivilegeType.objects.all()
    privileges = Privilege.objects.all()

    context = {
        "servers": servers,
        "title": "Donate",
        "privilegeTypes": privilegeTypes,
        "privileges": privileges
        }

    return render(request, 'donate.html', context)

def register(request):
    
    if request.method == "GET":
        form = RegisterForm()
        context = {
            "title": "Register",
            "form": form
        }
        
        return render(request, 'register.html', context)
    else:
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print("форма валидна")
            user = form.save(commit=False)
            user.save()
            profile = Profile(user=user)
            profile.save()

            messages.success(request, 'Регистрация прошла успешно :)')
            return redirect('login')
        else:
            print(form.errors)
            print("форма не валидна")
            print(form)
            return render(request, 'register.html', {'form': form})

def login(request):
    

    context = {
        "title": "Login"
    }
    
    return render(request, 'login.html', context)

@login_required(login_url="login")
def profile(request):

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print("Форма валидна")
            profile_data = Profile.objects.get(user=request.user)
            if "skin" in request.FILES:
                profile_data.skin=request.FILES['skin']
            if "image" in request.FILES:
                profile_data.image=request.FILES['image']
            profile_data.save()
        else:
            print("Форма не валидна")

    profile_data = Profile.objects.get(user=request.user)
    servers = Server.objects.all()
    profiles = Profile.objects.all()

    context = {
        "profile": profile_data,
        "servers": servers,
        "title" : "Profile",
        "profiles": profiles,

    }

    return render(request, 'profile.html', context)

def reg_profile(request):
    

    context = {
        "title": "Successfully"
    }

    return render(request, 'reg_profile.html', context)

def logout(request):


    context = {
        "title": "Successfully"
    }

    return render(request, 'logged_out.html', context)