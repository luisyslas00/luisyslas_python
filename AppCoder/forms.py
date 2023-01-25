from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  


class ContactoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField()

class NotaFormulario(forms.Form):
    mensaje = forms.CharField()

#Formulario registro

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}