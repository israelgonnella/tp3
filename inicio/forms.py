from django import forms

class CrearLibroFormulario (forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=20)
    año = forms.IntegerField()
    editorial = forms.CharField(max_length=20)
    
class BuscarLibroFormulario (forms.Form):
    titulo = forms.CharField(max_length=50, required=False)
    
class AgregarUsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    fecha_alta = forms.DateField(required=False)
    
class BuscarUsuarioFormulario (forms.Form):
    nombre = forms.CharField(max_length=50, required=False)
    