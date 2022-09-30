from datetime import datetime
from tkinter.tix import INTEGER
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from sitio.models import Barrio, Publicacion, Comentario, CustomUser
from sitio.forms import FormNuevaPublicacion, FormNuevoComentario


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

def filtropublicacion(request, filtro):
    barrios = Barrio.objects.all()

    if filtro == 'all' or filtro == 'reciente':
        publicaciones = Publicacion.objects.order_by('-publicationdate').filter(is_public=True).filter(state="Publicado")
    elif filtro == 'antiguo':
        publicaciones = Publicacion.objects.order_by('publicationdate').filter(is_public=True).filter(state="Publicado")
    elif filtro == 'like':
        publicaciones = Publicacion.objects.order_by('-likes').filter(is_public=True).filter(state="Publicado")
    else:
        barrio_filtro = Barrio.objects.filter(namebarrio=filtro)
        publicaciones = Publicacion.objects.order_by('-publicationdate').filter(location=barrio_filtro[0]).filter(is_public=True).filter(state="Publicado")

    vacio = False
    if len(publicaciones) == 0:
        vacio = True
    return render(request, 'noticiaspublicas.html', {'lista_publicaciones': publicaciones, 'vacia': vacio, 'lista_barrios': barrios})


@login_required(login_url='login')
def mibarrio(request):
    custom = CustomUser.objects.filter(user_id = request.user.id)
    mi_barrio = []
    barrios = []
    aceptado = 0
    vacio = False
    nombre_barrio = ""
    lista_solicitudes = []
    solicitudes_vacio = False
    #Controlar si el usuario es moderador
    is_moderator = False
    if request.user.groups.filter(name__in=['Moderador']):
        is_moderator = True
    if (custom[0].is_accept == 0):
        barrios = Barrio.objects.all().order_by("number")
        return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio, 'aceptado': aceptado, 'nombre_barrio': nombre_barrio, 'lista_solicitudes': lista_solicitudes, 'solicitudes_vacio': solicitudes_vacio})
    elif custom[0].is_accept == 1:
        aceptado = 1
        nombre_barrio = custom[0].barrio.namebarrio
        return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio, 'aceptado': aceptado, 'nombre_barrio': nombre_barrio, 'lista_solicitudes': lista_solicitudes, 'solicitudes_vacio': solicitudes_vacio})
    elif custom[0].is_accept == 2:
        mi_barrio = Publicacion.objects.order_by('-publicationdate').filter(location = custom[0].barrio).filter(state="Publicado")
        aceptado = 2
        lista_solicitudes = CustomUser.objects.filter(barrio = custom[0].barrio). filter(is_accept = 1)
        if len(mi_barrio) == 0:
            vacio = True 
        if len(lista_solicitudes) == 0:
            solicitudes_vacio = True  
        return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio, 'aceptado': aceptado, 'nombre_barrio': nombre_barrio, 'lista_solicitudes': lista_solicitudes, 'solicitudes_vacio': solicitudes_vacio, 'is_moderator': is_moderator})
    else:
        aceptado = 3
        nombre_barrio = custom[0].barrio.namebarrio
        barrios = Barrio.objects.all().order_by("number").exclude(namebarrio = nombre_barrio)
        return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio, 'aceptado': aceptado, 'nombre_barrio': nombre_barrio, 'lista_solicitudes': lista_solicitudes, 'solicitudes_vacio': solicitudes_vacio})

@login_required(login_url='login')
def nuevaPublicacion(request):
    if request.method == "POST":
        form = FormNuevaPublicacion(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.filter(id = request.user.id)
            custom = CustomUser.objects.filter(user_id = request.user.id)
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
                location = custom[0].barrio,
                )
            #return redirect('mibarrio')
            return redirect('homepage')
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


class detallePublicacion(View):
    def get(self, request, id_publicacion, *args, **kwargs):
        publicacion = Publicacion.objects.filter(id = id_publicacion)
        form = FormNuevoComentario()

        comentarios = Comentario.objects.filter(id_publicacion = id_publicacion).order_by('comentdate')

        context = {
            'lista_publicacion': publicacion,
            'lista_comentario': comentarios,
            'form': form,
        }

        return render(request, 'detallepublicacion.html', context)
    
    def post(self, request, id_publicacion, *args, **kwargs):
        publicacion = Publicacion.objects.filter(id = id_publicacion)
        form = FormNuevoComentario(request.POST)

        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.user = request.user.email
            nuevo_comentario.id_publicacion = id_publicacion
            nuevo_comentario.comentdate = datetime.today()
            nuevo_comentario.save()
        
        comentarios = Comentario.objects.filter(id_publicacion = id_publicacion).order_by('comentdate')

        context = {
            'lista_publicacion': publicacion,
            'lista_comentario': comentarios,
            'form': form,
        }

        return render(request, 'detallepublicacion.html',context)


@login_required(login_url='login')
def eliminarComentario(request, id_comentario):
    comentario = Comentario.objects.filter(id = id_comentario)
    comentario.delete()
    return redirect ('homepage')


def solicitud_unir(request, id_barrio):
    solicitante = CustomUser.objects.get(user_id = request.user.id)
    solicitante.is_accept = 1
    barrio = Barrio.objects.get(id = id_barrio)
    solicitante.barrio = barrio
    solicitante.save()
    return redirect('homepage')

def aceptar_solicitud(request, id_solicitud):
    solicitante = CustomUser.objects.get(user_id = id_solicitud)
    solicitante.is_accept = 2
    solicitante.save()
    return redirect('homepage')


def rechazar_solicitud(request, id_solicitud):
    solicitante = CustomUser.objects.get(user_id = id_solicitud)
    solicitante.is_accept = 3
    solicitante.save()
    return redirect('homepage')