from django.shortcuts import render
from django.contrib import auth

def homepage(request):
    return render(request, 'homepage.html', {})

def mibarrio(request):
    return render(request, 'mibarrio.html', {})

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def nuevaPublicacion(request):
    return render(request, 'nueva_publicacion.html', {})