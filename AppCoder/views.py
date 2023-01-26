from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import ContactoFormulario, PeliculaFormulario, NotaFormulario, UserRegisterForm
from AppCoder.models import Contacto, GuardarPelicula, AgendarNota

# Create your views here.

def inicio(request):
    return render(request,'AppCoder/inicio.html')

def contactos(request):
    if request.method == "POST":
        miFormulario = ContactoFormulario(request.POST)
        print(miFormulario) 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            contacto = Contacto(nombre=informacion["nombre"], apellido=informacion["apellido"], telefono = informacion["telefono"],email = informacion["email"])
            contacto.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ContactoFormulario()
 
    return render(request, "AppCoder/contactos.html", {"miFormulario": miFormulario})



def peliculas(request):
    if request.method == "POST":
        miFormulario = PeliculaFormulario(request.POST)
        print(miFormulario) 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pelicula = GuardarPelicula(nombre=informacion["nombre"])
            pelicula.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = PeliculaFormulario()
 
    return render(request, "AppCoder/peliculas.html", {"miFormulario": miFormulario})

def notas(request):
    if request.method == "POST":
        miFormulario = NotaFormulario(request.POST)
        print(miFormulario) 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nota = AgendarNota(mensaje=informacion["mensaje"])
            nota.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = NotaFormulario()
 
    return render(request, "AppCoder/notas.html", {"miFormulario": miFormulario})

#Buscar y Resultado - Contactos

def buscarContacto(request):
    return render(request,"AppCoder/buscarContacto.html")

def resultadoContacto(request):
    if request.GET["nombre"]:
        contacto = request.GET['nombre']
        contactos = Contacto.objects.filter(nombre__icontains=contacto)
        return render(request, "AppCoder/buscarContacto.html",{"contactos":contactos, "contacto": contacto})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#Buscar y Resultados - Peliculas

def buscarPelicula(request):
    return render(request,"AppCoder/buscarPelicula.html")

def resultadoPelicula(request):
    if request.GET["pelicula"]:
        pelicula = request.GET['pelicula']
        peliculas = GuardarPelicula.objects.filter(nombre__icontains=pelicula)
        return render(request, "AppCoder/buscarPelicula.html",{"peliculas":peliculas, "pelicula": pelicula})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#Buscar y Resultados - Notas

def buscarNota(request):
    return render(request,"AppCoder/buscarNota.html")

def resultadoNota(request):
    if request.GET["nota"]:
        nota = request.GET['nota']
        notas = AgendarNota.objects.filter(mensaje__icontains=nota)
        return render(request, "AppCoder/buscarNota.html",{"notas":notas, "nota": nota})
    else: 
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

#CRUD Contactos - Lista, Eliminar y Editar

def listaContactos(request):
    contactos = Contacto.objects.all()
    contexto = {"contactos":contactos}
    return render(request,"AppCoder/listaContactos.html",contexto)

def eliminarContacto(request,contacto_nombre):
    contacto = Contacto.objects.get(nombre=contacto_nombre)
    contacto.delete()
    contactos = Contacto.objects.all()
    contexto = {"contactos":contactos}
    return render(request,"AppCoder/listaContactos.html",contexto)

def editarContacto(request,contacto_nombre):
    contacto= Contacto.objects.get(nombre=contacto_nombre)
    if request.method == "POST":
        miFormulario = ContactoFormulario(request.POST)
        print(miFormulario)
        if miFormulaio.is_valid:
            informacion = miFormulario.cleaned_data
            contacto.nombre = informacion['nombre']
            contacto.apellido = informacion['apellido']
            contacto.telefono = informacion['telefono']
            contacto.email = informacion['email']
            contacto.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = ContactoFormulario(initial={'nombre':contacto.nombre,'apellido':contacto.apellido,'telefono':contacto.telefono,'email':contacto.email})
    return render(request,"AppCoder/editarContacto.html",{"miFormulario":miFormulario,"contacto_nombre":contacto_nombre})

# CRUD Peliculas - Listas, Eliminar y Editar

def listaPeliculas(request):
    peliculas = GuardarPelicula.objects.all()
    contexto = {"peliculas":peliculas}
    return render(request,"AppCoder/listaPeliculas.html",contexto)

def eliminarPelicula(request,pelicula_nombre):
    pelicula = GuardarPelicula.objects.get(nombre=pelicula_nombre)
    pelicula.delete()
    peliculas = GuardarPelicula.objects.all()
    contexto = {"peliculas":peliculas}
    return render(request,"AppCoder/listaPeliculas.html",contexto)


def editarPelicula(request,pelicula_nombre):
    pelicula= GuardarPelicula.objects.get(nombre=pelicula_nombre)
    if request.method == "POST":
        miFormulario = PeliculaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pelicula.nombre = informacion['nombre']
            pelicula.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = PeliculaFormulario(initial={'nombre':pelicula.nombre})
    return render(request,"AppCoder/editarPelicula.html",{"miFormulario":miFormulario,"pelicula_nombre":pelicula_nombre})

#CRUD Notas - Listas, Eliminar y Editar

def listaNotas(request):
    notas = AgendarNota.objects.all()
    contexto = {"notas":notas}
    return render(request,"AppCoder/listaNotas.html",contexto)


def eliminarNota(request,nota_mensaje):
    nota = AgendarNota.objects.get(mensaje=nota_mensaje)
    nota.delete()
    notas = AgendarNota.objects.all()
    contexto = {"notas":notas}
    return render(request,"AppCoder/listaNotas.html",contexto)


def editarNota(request,nota_mensaje):
    nota= AgendarNota.objects.get(mensaje=nota_mensaje)
    if request.method == "POST":
        miFormulario = NotaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            nota.mensaje = informacion['mensaje']
            nota.save()
            return render(request,"AppCoder/inicio.html")
    else:
        miFormulario = NotaFormulario(initial={'mensaje':nota.mensaje})
    return render(request,"AppCoder/editarNota.html",{"miFormulario":miFormulario,"nota_mensaje":nota_mensaje})

#CBV

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Contactos

class ContactoList(ListView):
    model = Contacto
    template_name = "AppCoder/contactos_list.html"

class ContactoDetalle(DetailView):
    model = Contacto
    template_name = "AppCoder/contacto_detalle.html"

class ContactoCreacion(CreateView):
    model = Contacto
    success_url = "/AppCoder/contactos/list"
    fields = ['nombre','apellido','telefono','email']

class ContactoUpdate(UpdateView):
    model = Contacto
    success_url = "/AppCoder/contactos/list"
    fields = ['nombre','apellido','telefono','email']

class ContactoDelete(DeleteView):
    model = Contacto
    success_url = "/AppCoder/contactos/list"

#Notas

# class NotaList(ListView):
#     model = AgendarNota
#     template_name = "AppCoder/notas_list.html"

# class NotaDetalle(DetailView):
#     model = AgendarNota
#     template_name = "AppCoder/nota_detalle.html"

# class NotaCreacion(CreateView):
#     model = AgendarNota
#     success_url = "/AppCoder/notas/list"
#     fields = ['mensaje']

# class NotaUpdate(UpdateView):
#     model = AgendarNota
#     success_url = "/AppCoder/notas/list"
#     fields = ['mensaje']

# class NotaDelete(DeleteView):
#     model = AgendarNota
#     success_url = "/AppCoder/notas/list"

# #Peliculas

# class PeliculaList(ListView):
#     model = GuardarPelicula
#     template_name = "AppCoder/peliculas_list.html"

# class PeliculaDetalle(DetailView):
#     model = GuardarPelicula
#     template_name = "AppCoder/pelicula_detalle.html"

# class PeliculaCreacion(CreateView):
#     model = GuardarPelicula
#     success_url = "/AppCoder/peliculas/list"
#     fields = ['nombre']

# class PeliculaUpdate(UpdateView):
#     model = GuardarPelicula
#     success_url = "/AppCoder/peliculas/list"
#     fields = ['nombre']

# class PeliculaDelete(DeleteView):
#     model = GuardarPelicula
#     success_url = "/AppCoder/peliculas/list"

#LOGIN

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario,password=contrasenia)
            if user is not None:
                login(request,user)
                return render(request,'AppCoder/inicio.html',{'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request,'AppCoder/login.html',{'mensaje':"Error, datos incorrectos",'form':form})
        else:
            return render(request,"AppCoder/login.html",{'mensaje':"Error, formulario erroneo",'form':form})
    form = AuthenticationForm()
    return render(request,"AppCoder/login.html",{'form':form})

#REGISTER

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/registro.html",{'mensaje':'Usuario creado correctamente','form':form})
    else:
        form = UserRegisterForm()
    return render(request,"AppCoder/registro.html",{'form':form})

#Decoradores

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):
    return render(request,"AppCoder/inicio.html")

#Editar Perfil

from AppCoder.forms import UserEditForm

# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render(request, "AppCoder/inicio.html",{'mensaje':'Su perfil ha sido actualizado'})
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
