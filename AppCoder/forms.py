from django import forms
 
class ContactoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField()

class NotaFormulario(forms.Form):
    mensaje = forms.CharField()