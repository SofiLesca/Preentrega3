from django import forms

class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=80)
    apellido=forms.CharField(required=True, max_length=180)
    email=forms.CharField(required=True, max_length=300)
    dni=forms.CharField(required=True, max_length=32)
    telefono=forms.CharField(required=True, max_length=25)
    dni=forms.DateField(required=True,)
    