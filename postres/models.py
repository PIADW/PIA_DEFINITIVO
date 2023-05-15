from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=60)
    presentacion = models.CharField(max_length=45)
    precio = models.FloatField()
    Sabor = models.CharField(max_length=55)

    def __str__(self):
        return self.descripcion

class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=45)
    potencia = models.IntegerField()
   

    def __str__(self):
        return self.marca