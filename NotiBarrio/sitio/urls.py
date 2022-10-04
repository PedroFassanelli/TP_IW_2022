from django.urls import path, include
from . import views

urlpatterns = [
    path('mibarrio/', views.mibarrio, name='mibarrio'),
    path('notipublicas/', views.notipublicas, name='notipublicas'),
    path('nuevapublicacion/', views.nuevaPublicacion, name='nuevapublicacion'),
    path('edit_publicacion/<int:id_publicacion>/', views.editarPublicacion, name='edit_publicacion'),
    path('eliminar/<int:id_publicacion>/', views.eliminarPublicacion, name='eliminar'),
    path('detallepublicacion/<int:id_publicacion>/', views.detallePublicacion.as_view(), name='detallepublicacion'),
    path('filtro/<str:filtro>/', views.filtropublicacion, name='filtropublicacion'),
    path('eliminarcomentario/<int:id_comentario>/', views.eliminarComentario, name='eliminarcomentario'),
    path('solicitarunirse/<int:id_barrio>/', views.solicitud_unir, name='solicitarunirse'),
    path('aceptarsolicitud/<int:id_solicitud>/', views.aceptar_solicitud, name='aceptarsolicitud'),
    path('rechazarsolicitud/<int:id_solicitud>/', views.rechazar_solicitud, name='rechazarsolicitud'),
    path('search/', include('haystack.urls')),
]