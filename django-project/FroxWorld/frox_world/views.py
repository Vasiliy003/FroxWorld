from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    

    context = {
        "title": "Register"
    }
    
    return render(request, 'register.html', context)

def login(request):
    

    context = {
        "title": "Login"
    }
    
    return render(request, 'login.html', context)

@login_required(login_url="login")
def profile(request):
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