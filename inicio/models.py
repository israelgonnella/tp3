from django.db import models

# Create your models here.

class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=20)
    año = models.IntegerField()
    editorial = models.CharField(max_length=20)
    
    def __str__(self):
        return f'TITULO: {self.titulo}  -  AUTOR: {self.autor}'
    
class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=20)
    dni = models.IntegerField()
    fecha_alta = models.DateField()
    
    def __str__(self):
        return f'NOMBRE: {self.nombre}  -  DNI: {self.dni}'
