from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#JUEGOS-PAGOS-------->

#JUEGOS-PAGOS-------->
class Stock(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.IntegerField()

class PayGames(models.Model): 
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=500)
    lanzamiento = models.DateField()
    clasificacion = models.IntegerField()
    costo = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}, {self.costo}'
        

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
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre}'
    
class Carrito(models.Model):
    cantidad_articulos = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)