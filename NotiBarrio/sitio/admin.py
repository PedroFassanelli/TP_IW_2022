from django.contrib import admin
from .models import Usuario, Barrio, Publicacion

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
    list_per_page = 10

@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
    search_fields = ('id', 'namebarrio', 'number')
    list_display = ('id', 'namebarrio', 'number')
    list_display_links = ('id', 'namebarrio')
    list_per_page = 10

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title', 'user', 'location')
    list_display = ('id', 'title', 'user', 'location')
    list_display_links = ('id', 'title')
    list_per_page = 10