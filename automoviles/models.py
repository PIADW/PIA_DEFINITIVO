from django.db import models

# Create your models here.
class Unidad(models.Model):
    Placa = models.CharField(max_length=10)
    Marca = models.CharField(max_length=40)
    Modelo = models.CharField(max_length=50)
    Año = models.IntegerField()
    Conductor = models.CharField(max_length=80)

    def __str__(self):
        return self.Conductor