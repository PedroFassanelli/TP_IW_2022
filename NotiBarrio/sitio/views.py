from datetime import datetime
from hashlib import new
from sre_parse import State
from time import timezone
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sitio.models import Barrio, Publicacion
from sitio.forms import FormNuevaPublicacion


def homepage(request):
    publicaciones = Publicacion.objects.order_by('-publicationdate').filter(is_public=True).filter(state="Publicado")[:5]
    vacio = False
    if len(publicaciones) == 0:
        vacio = True
    return render(request, 'homepage.html', {'lista_publicaciones': publicaciones, 'vacia': vacio})


def notipublicas(request):
    publicaciones = Publicacion.objects.order_by('-publicationdate').filter(is_public=True).filter(state="Publicado")
    barrios = Barrio.objects.all()
    vacio = False
    if len(publicaciones) == 0:
        vacio = True
    return render(request, 'noticiaspublicas.html', {'lista_publicaciones': publicaciones, 'vacia': vacio, 'lista_barrios': barrios})


@login_required(login_url='login')
def mibarrio(request):
    barrios = Barrio.objects.all().order_by("number")
    mi_barrio = Publicacion.objects.order_by('-publicationdate').filter(state="Publicado")
    vacio = False
    if len(mi_barrio) == 0:
        vacio = True
    return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio})


@login_required(login_url='login')
def nuevaPublicacion(request, id_user):
    if request.method == "POST":
        form = FormNuevaPublicacion(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.filter(id = id_user)
            new_publicacion = form.save(commit=False)
            Publicacion.objects.create(
                publicationdate = datetime.today(),
                state = 'Publicado',
                title = new_publicacion.title,
                text = new_publicacion.text,
                image_one = new_publicacion.image_one,
                image_two = new_publicacion.image_two,
                image_three = new_publicacion.image_three,
                is_public = new_publicacion.is_public,
                user = usuario[0].email,
                location = new_publicacion.location,
                )
            return redirect('mibarrio')
    else:
        form = FormNuevaPublicacion()
    return render(request, 'nueva_publicacion.html', {"form": form})


@login_required(login_url='login')
def editarPublicacion(request, id_publicacion):
    context = {}
    try:
        publicacion = Publicacion.objects.get(pk = id_publicacion)
    except Publicacion.DoesNotExist:
        messages.error(request, f"La publicación no existe")
        return redirect('homepage')
    context['instance'] = publicacion
    if request.method == 'POST':
        form = FormNuevaPublicacion(request.POST, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FormNuevaPublicacion(instance=publicacion)
    context['form'] = form
    return render(request, 'edit_publicacion.html', context=context)


@login_required(login_url='login')
def eliminarPublicacion(request, id_publicacion):
    publicacion = Publicacion.objects.filter(id = id_publicacion)
    publicacion.delete()
    return redirect ('homepage')


def detallePublicacion(request, id_publicacion):
    publicacion = Publicacion.objects.filter(id = id_publicacion)
    return render(request, 'detallepublicacion.html', {"lista_publicacion": publicacion})