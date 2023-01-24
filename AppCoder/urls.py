from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('contactos',views.contactos, name="Contactos"),
    path('peliculas',views.peliculas, name="Peliculas"),
    path('notas',views.notas,name="Notas"),
    path('buscarContacto', views.buscarContacto , name="BuscarContacto"),
    path('resultadoContacto/', views.resultadoContacto),
    path('buscarPelicula', views.buscarPelicula , name="BuscarPelicula"),
    path('resultadoPelicula/', views.resultadoPelicula),
    path('buscarNota', views.buscarNota , name="BuscarNota"),
    path('resultadoNota/', views.resultadoNota),
    path('listaContactos',views.listaContactos,name= "ListaContactos"),
    path('eliminarContacto/<contacto_nombre>/',views.eliminarContacto,name="EliminarContacto"),
    path('editarContacto/<contacto_nombre>/',views.editarContacto,name="EditarContacto")
]