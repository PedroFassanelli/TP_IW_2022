import email
#from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    Estados = (
        ('Registrado', 'Usuario normal'),
        ('Moderador', 'Usuario con permisos'),
        ('Baneado', 'Usuario baneado'),
        ('Eliminado', 'Usuario eliminado'),
    )
    first_name = User.first_name
    last_name = User.last_name
    email = User.email
    password = User.password
    denounced = models.IntegerField(default= 0)
    born = models.DateField(null= False, blank= False)
    location = models.CharField(max_length= 25, null= False, blank= False)
    state = models.CharField(max_length=25, choices= Estados, default= 'Registrado')

class Barrio(models.Model):
    pass

class Publicacion(models.Model):
    Estados = (
        ('Borrador', 'Borrador no publicado'),
        ('Publicado', 'Publicado en el sitio'),
        ('Eliminado', 'Publicacion eliminada'),
    )
    location = models.ForeignKey(Barrio, blank= False, null= False, on_delete=models.CASCADE)
    denounced = models.IntegerField(default= 0)
    user = User.email
    title = models.CharField(max_length= 50)
    text = models.TextField(max_length= 250)
    publicationdate = models.DateTimeField()
    is_public = models.BooleanField(default= True)
    state = models.CharField(max_length=25, choices= Estados, default= 'Borrador')
    likes = models.IntegerField(default= 0)
    dislikes = models.IntegerField(default= 0)