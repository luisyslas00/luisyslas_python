from django.urls import path
from AppCoder import views
#LOGOUT
from django.contrib.auth.views import LogoutView

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
    path('editarContacto/<contacto_nombre>/',views.editarContacto,name="EditarContacto"),
    path('listaPeliculas',views.listaPeliculas,name= "ListaPeliculas"),
    path('eliminarPelicula/<pelicula_nombre>/',views.eliminarPelicula,name="EliminarPelicula"),
    path('editarPelícula/<pelicula_nombre>/',views.editarPelicula,name="EditarPelicula"),
    path('listaNotas',views.listaNotas,name="ListaNotas"),
    path('eliminarNota/<nota_mensaje>/',views.eliminarNota,name="EliminarNota"),
    path('editarNota/<nota_mensaje>/',views.editarNota,name="EditarNota"),
    #CBV-- Contactos
    path('contactos/list',views.ContactoList.as_view(),name="List"),
    path(r'^(?P<pk>\d+)$', views.ContactoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ContactoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ContactoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ContactoDelete.as_view(), name='Delete'),
    #CBV-- Peliculas
    # path('peliculas/list',views.PeliculaList.as_view(),name="ListPelicula"),
    # path(r'^(?P<pk>\d+)$', views.PeliculaDetalle.as_view(), name='DetailPelicula'),
    # path(r'^nuevo$', views.PeliculaCreacion.as_view(), name='NewPelicula'),
    # path(r'^editar/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name='EditPelicula'),
    # path(r'^borrar/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name='DeletePelicula'),
    # #CBV-- Notas
    # path('notas/list',views.NotaList.as_view(),name="ListNota"),
    # path(r'^(?P<pk>\d+)$', views.NotaDetalle.as_view(), name='DetailNota'),
    # path(r'^nuevo$', views.NotaCreacion.as_view(), name='NewNota'),
    # path(r'^editar/(?P<pk>\d+)$', views.NotaUpdate.as_view(), name='EditNota'),
    # path(r'^borrar/(?P<pk>\d+)$', views.NotaDelete.as_view(), name='DeleteNota')
    
    #LOGIN
    path('login', views.login_request,name='Login'),
    #REGISTER
    path('register',views.register,name='Register'),
    #LOGOUT
    path('logout',LogoutView.as_view(template_name="AppCoder/logout.html"),name='Logout'),
]