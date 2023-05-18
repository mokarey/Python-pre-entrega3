from django.db import models
from django import forms
from PIL import Image

# Create your models here.
#JUEGOS-PAGOS-------->

#JUEGOS-PAGOS-------->
class Stock(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.IntegerField()

class PayGames(models.Model): 
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=256)
    lanzamiento = models.DateField(max_length=20)
    clasificacion = models.IntegerField()
    costo = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.costo}, {self.imagen.name}'
        

#JUEGOS-GRATIS-------->
class FreeStock(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.IntegerField()

class FreeGames(models.Model):
    nombre =models.CharField(max_length=100)
    genero =models.CharField(max_length=40)
    descripcion = models.CharField(max_length=256)
    lanzamiento = models.DateField(max_length=20)
    clasificacion = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'