from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from sitio.forms import FormNuevaPublicacion 

def homepage(request):
    return render(request, 'homepage.html')


def notipublicas(request):
    return render(request, 'noticiaspublicas.html')


@login_required(login_url='login')
def mibarrio(request):
    return render(request, 'mibarrio.html')


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