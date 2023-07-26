from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login (request):
      
  formulario= AuthenticationForm()  
  return render (request, 'lectores/login.html', {'formulario': formulario})