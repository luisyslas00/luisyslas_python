from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length =30)
    apellido = models.CharField(max_length = 30)
    telefono = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Telefono: - {self.telefono} - Correo: {self.email}"

class GuardarPelicula(models.Model):
    nombre = models.CharField(max_length = 50)
    def __str__(self):
        return f"Pelicula: {self.nombre}"

class AgendarNota(models.Model):
    mensaje = models.CharField(max_length = 200)
    def __str__(self):
        return f"Mensaje: {self.mensaje}"

class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank=True)