from multiprocessing import context
from django.shortcuts import render, redirect
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
            form = FromLogin(data = request.POST)
            validar_email = form.email
            validar_password = form.password
            if form.is_valid():
                user = authenticate(email=validar_email, password=validar_password)
                if user is not None:
                    if user.is_active:
                        auth.login(request, user)
                        next = request.POST.get('next')
                        if next:
                            return redirect(request.POST.get('next'))
                        else:
                            return redirect('homepage')
            else:
                lista_usuario = User.objects.all()
                valido = False
                for x in lista_usuario:
                    if (x.email == validar_email):
                        valido = True
                        break
                if valido:
                    if (not user.is_active):
                        messages.success('El usuario no está activo, verifique su email')
                    else:
                        messages.success('La contraseña ingresada es incorrecta')
        else:
            form = FromLogin()
        context = {'form': form, 'messages': messages}
        return render(request, 'login.html', context)
    else:
        return redirect('homepage') 

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = FromCrearUsuario(data = request.POST)
            if form.is_valid():
                validar_email = form.cleaned_data['email']
                lista_usuarios = User.objects.all()
                valido = True
                for x in lista_usuarios:
                    if validar_email == x.email:
                        valido = False
                        break
                if valido:
                    guardar = Usuario()
                    guardar.email = form.cleaned_data['email']
                    guardar.first_name = form.cleaned_data['first_name']
                    guardar.last_name = form.cleaned_data['last_name']
                    guardar.password = form.cleaned_data['password']
                    guardar.location = form.cleaned_data['location']
                    guardar.is_active = False
                    guardar.save()
                    return redirect('login')
                else:
                    messages.success('El email ingresado ya fue utilizado')
                    form = FromCrearUsuario(data = request.POST)
            else:
                form = FromCrearUsuario(data = request.POST)
        else:
            form = FromCrearUsuario()
        context = {'form': form, 'messages': messages}
        return render(request, 'register.html', context)
    else:
        return redirect('homepage')

def notipublicas(request):
    return render(request, 'noticiaspublicas.html', {})

@login_required(login_url= 'login')
def mibarrio(request):
    return render(request, 'mibarrio.html', {})

@login_required(login_url= 'login')
def nuevaPublicacion(request):
    return render(request, 'nueva_publicacion.html', {})