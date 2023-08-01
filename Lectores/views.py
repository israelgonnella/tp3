from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login as django_login
from Lectores.form import MiFormularioDeCrecionDeUsurios

# Create your views here.
 
def login (request):
  
  if request.method == 'POST':
    formulario = AuthenticationForm(request, data=request.POST)
    if formulario.is_valid():
      usuario = formulario.cleaned_data['username']
      contrasenia = formulario.cleaned_data['password']
      
      user = authenticate(username=usuario, password=contrasenia)
      
      django_login(request, user)
      return redirect ('inicio:inicio')
      
    else:
        return render (request, 'lectores/login.html', {'formulario': formulario})
   
  formulario = AuthenticationForm()     
  return render (request, 'lectores/login.html', {'formulario': formulario})

def registrarse (request):
  
  if request.method == 'POST':
    formulario = MiFormularioDeCrecionDeUsurios (request.POST)
    if formulario.is_valid():
       formulario.save()
       return redirect ('lectores:login.html')
    else:
        return render (request, 'lectores/registro.html', {'formulario': formulario})

  formulario = MiFormularioDeCrecionDeUsurios()
  return render (request, 'lectores/registro.html', {'formulario': formulario})