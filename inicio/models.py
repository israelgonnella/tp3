from django.db import models

# Create your models here.

class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=20)
    año = models.IntegerField()
    editorial = models.CharField(max_length=20)
    
class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=20)
    dni = models.IntegerField()
    fecha_alta = models.DateField()
