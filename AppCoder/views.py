from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import ContactoFormulario, PeliculaFormulario, NotaFormulario
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
        if miFormulario.is_valid:
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
