from django.contrib import admin
from .models import Barrio, Publicacion, Comentario, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'customuser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

'''@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email', 'first_name', 'last_name')
    list_display = ('id', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
    list_per_page = 10'''

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

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ('id', 'text', 'user')
    list_display = ('id', 'text', 'user')
    list_display_links = ('id', 'user','text')
    list_per_page = 10