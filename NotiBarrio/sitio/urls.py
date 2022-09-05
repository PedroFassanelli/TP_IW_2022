from django.urls import path
from . import views

urlpatterns = [
    path('mibarrio/', views.mibarrio, name='mibarrio'),
    path('notipublicas/', views.notipublicas, name='notipublicas'),
    path('nuevapublicacion/<int:id_user>/', views.nuevaPublicacion, name='nuevapublicacion'),
    path('edit_publicacion/<int:id_publicacion>/', views.editarPublicacion, name='edit_publicacion'),
    path('eliminar/<int:id_publicacion>/', views.eliminarPublicacion, name='eliminar'),
    path('detallepublicacion/<int:id_publicacion>/', views.detallePublicacion, name='detallepublicacion'),
]