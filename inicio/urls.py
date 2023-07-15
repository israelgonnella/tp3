from django.urls import path
from inicio import views

app_name= 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('usuario/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuario/', views.lista_usuarios, name='usuario'),
    path('libros/<int:pk>/', views.DetalleLibro.as_view(), name='detalle_libros'),
    path('libros/<int:pk>/modificar/', views.ModificarLibro.as_view(), name='modificar_libros'),
    path('libros/<int:pk>/eliminar/', views.EliminarLibro.as_view(), name='eliminar_libros'),
]
