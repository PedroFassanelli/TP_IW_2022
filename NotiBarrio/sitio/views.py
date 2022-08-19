from django.shortcuts import render
from django.contrib import auth
from sitio.models import *
from sitio.forms import *
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

@login_required(login_url= 'login')
def mibarrio(request):
    return render(request, 'mibarrio.html', {})

@login_required(login_url= 'login')
def nuevaPublicacion(request):
    return render(request, 'nueva_publicacion.html', {})