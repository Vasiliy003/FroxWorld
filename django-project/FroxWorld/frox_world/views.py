from django.shortcuts import render
from django.http import HttpResponse

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