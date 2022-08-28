from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')


def notipublicas(request):
    return render(request, 'noticiaspublicas.html')


@login_required(login_url='logueo')
def mibarrio(request):
    return render(request, 'mibarrio.html')


@login_required(login_url='logueo')
def nuevaPublicacion(request):
    return render(request, 'nueva_publicacion.html')