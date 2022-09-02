from django.urls import path
from . import views

urlpatterns = [
    path('mibarrio/', views.mibarrio, name='mibarrio'),
    path('notipublicas/', views.notipublicas, name='notipublicas'),
    path('nuevapublicacion/', views.nuevaPublicacion, name='nuevapublicacion'),
    path('edit_publicacion/', views.editarPublicacion, name='edit_publicacion'),
]