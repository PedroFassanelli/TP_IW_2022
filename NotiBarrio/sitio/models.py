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

    def __str__(self):
        text = "{0}, ({1})"
        return text.format(self.email, (self.first_name + ' ' + self.last_name))



class Barrio(models.Model):
    namebarrio = models.CharField(max_length=50, default='None')
    number = models.PositiveIntegerField(default= 0)

    def __str__(self):
        return self.namebarrio

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, blank=True, on_delete=models.DO_NOTHING)

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
    is_public = models.BooleanField(default= False)
    state = models.CharField(max_length=25, choices= Estados, default= 'Borrador')
    likes = models.IntegerField(default= 0)
    dislikes = models.IntegerField(default= 0)
    image_one = models.ImageField(upload_to = "static/sitio/multimedias/", null= True, blank = True, default='static/sitio/multimedias/logo.png')
    image_two = models.ImageField(upload_to = "static/sitio/multimedias/", null= True, blank = True)
    image_three = models.ImageField(upload_to = "static/sitio/multimedias/", null= True, blank = True)

    def __str__(self):
        text = "{0}, ({1})"
        return text.format(self.title, (self.user + ' ' + self.location))