from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('usuario/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuario/', views.lista_usuarios, name='usuario'),
]
