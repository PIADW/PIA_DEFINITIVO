from django.db import models

# Create your models here.
class Producto(models.Model):
    Descripcion = models.CharField(max_length=60)
    Presentacion = models.CharField(max_length=45)
    Precio = models.FloatField()
    Sabor = models.CharField(max_length=55)

    def __str__(self):
        return self.Descripcion

class EquipoDeCocina(models.Model):
    Nombre = models.CharField(max_length=60)
    Marca = models.CharField(max_length=45)
    Potencia = models.IntegerField()
    Antiguedad = models.IntegerField()

    def __str__(self):
        return self.Nombre