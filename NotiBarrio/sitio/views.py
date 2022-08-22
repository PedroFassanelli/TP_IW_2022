from multiprocessing import context
from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from sitio.models import *
from sitio.forms import *
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html', {})

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = FromLogin(data = request.Post)
            if form.is_valid():
                validar_email = form.cleaned_data['email']
                validar_password = form.cleaned_data['password']

                messages.success(request, 'Usuario Logeado')
        else:
            form = FromLogin()
    
    context = {'form': form, 'messages': messages}
    return render(request, 'login.html', context)

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = FromCrearUsuario(data = request.POST)
            if form.is_valid():
                validar = form.cleaned_data['email']
                
                messages.success(request, 'Usuario creado')
        else:
            form = FromCrearUsuario()
    
    context = {'form': form, 'messages': messages}
    return render(request, 'register.html', context)

def notipublicas(request):
    return render(request, 'noticiaspublicas.html', {})

@login_required(login_url= 'login')
def mibarrio(request):
    return render(request, 'mibarrio.html', {})

@login_required(login_url= 'login')
def nuevaPublicacion(request):
    return render(request, 'nueva_publicacion.html', {})