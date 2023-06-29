from django.shortcuts import render, redirect
from inicio.forms import CrearLibroFormulario, BuscarLibroFormulario, BuscarUsuarioFormulario, AgregarUsuarioFormulario
from inicio.models import Libro, Usuario
# Create your views here.

def inicio(request):
    return render(request,'inicio/inicio.html')

def crear_libro(request):
    
    if request.method == 'POST':
        formulario = CrearLibroFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            libro = Libro(titulo=informacion['titulo'],autor=informacion['autor'],año=informacion['año'],editorial=informacion['editorial'])
            libro.save()
            return redirect('inicio:lista_libros')
        else:
            return render(request,'inicio/crear_libro.html', {'formulario': formulario})
    
    formulario = CrearLibroFormulario()
    return render(request,'inicio/crear_libro.html', {'formulario': formulario})

def lista_libros(request):
    formulario = BuscarLibroFormulario(request.GET)
    if formulario.is_valid():
            titulo_buscar = formulario.cleaned_data['titulo']
            listado_libros = Libro.objects.filter(titulo__icontains=titulo_buscar)
    formulario = BuscarLibroFormulario()
    return render(request,'inicio/lista_libros.html', {'formulario': formulario, 'Libros': listado_libros})

def agregar_usuario(request):
    
    if request.method == 'POST':
        formulario = AgregarUsuarioFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = Usuario(nombre=informacion['nombre'],direccion=informacion['direccion'],dni=informacion['dni'],fecha_alta=informacion['fecha_alta'])
            usuario.save()
            return redirect('inicio:usuario')
        else:
            return render(request,'inicio/agregar_usuario.html', {'formulario': formulario})
    
    formulario = AgregarUsuarioFormulario()
    return render(request,'inicio/agregar_usuario.html', {'formulario': formulario})

def lista_usuarios(request):
    formulario = BuscarUsuarioFormulario(request.GET)
    if formulario.is_valid():
            nombre_buscar = formulario.cleaned_data['nombre']
            listado_usuarios = Usuario.objects.filter(nombre__icontains=nombre_buscar)
    formulario = BuscarUsuarioFormulario()
    return render(request,'inicio/usuario.html', {'formulario': formulario, 'Usuario': listado_usuarios})