from django.urls import path
from AppCoder import views
#LOGOUT
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name="Inicio"),
    path('contactos',views.contactos, name="Contactos"),
    path('peliculas',views.peliculas, name="Peliculas"),
    path('aboutMe',views.aboutMe, name="AboutMe"),
    path('notas',views.notas,name="Notas"),
    path('buscarContacto', views.buscarContacto , name="BuscarContacto"),
    path('resultadoContacto/', views.resultadoContacto),
    path('buscarPelicula', views.buscarPelicula , name="BuscarPelicula"),
    path('resultadoPelicula/', views.resultadoPelicula),
    path('buscarNota', views.buscarNota , name="BuscarNota"),
    path('resultadoNota/', views.resultadoNota),
    path('listaContactos',views.listaContactos,name= "ListaContactos"),
    path('eliminarContacto/<contacto_nombre>/',views.eliminarContacto,name="EliminarContacto"),
    path('editarContacto/<contacto_nombre>/',views.editarContacto,name="EditarContacto"),
    path('listaPeliculas',views.listaPeliculas,name= "ListaPeliculas"),
    path('eliminarPelicula/<pelicula_nombre>/',views.eliminarPelicula,name="EliminarPelicula"),
    path('editarPelícula/<pelicula_nombre>/',views.editarPelicula,name="EditarPelicula"),
    path('listaNotas',views.listaNotas,name="ListaNotas"),
    path('eliminarNota/<nota_mensaje>/',views.eliminarNota,name="EliminarNota"),
    path('editarNota/<nota_mensaje>/',views.editarNota,name="EditarNota"),
    path('contactos/list',views.ContactoList.as_view(),name="List"),
    path(r'^(?P<pk>\d+)$', views.ContactoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ContactoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ContactoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ContactoDelete.as_view(), name='Delete'),    
    path('login', views.login_request,name='Login'),
    path('register',views.register,name='Register'),
    path('logout',LogoutView.as_view(template_name="AppCoder/logout.html"),name='Logout'),

    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
]