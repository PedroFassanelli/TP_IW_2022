from sre_parse import State
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sitio.models import Barrio, Publicacion
from sitio.forms import FormNuevaPublicacion 

def homepage(request):
    return render(request, 'homepage.html')


def notipublicas(request):
    return render(request, 'noticiaspublicas.html')


@login_required(login_url='login')
def mibarrio(request):
    barrios = Barrio.objects.all().order_by("number")
    mi_barrio = Publicacion.objects.filter(state="Publicado")
    vacio = False
    if len(mi_barrio) == 0:
        vacio = True
    return render(request, 'mibarrio.html', {'lista_barrios': barrios, 'lista_mibarrio': mi_barrio, 'vacia': vacio})


@login_required(login_url='login')
def nuevaPublicacion(request):
    if request.method == "POST":
        form = FormNuevaPublicacion(request.POST, request.FILES)
        if form.is_valid():
            new_publicacion = form.save(commit=False)
            new_publicacion.user = request.user
            new_publicacion.save()
            return redirect('mis_articulos')
    else:
        form = FormNuevaPublicacion()
    return render(request, 'nueva_publicacion.html', {"form": form})