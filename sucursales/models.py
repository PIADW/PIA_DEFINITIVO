from django.db import models

# Create your models here.
class Tienda(models.Model):
    NombreSuc =models.CharField(max_length=80)
    Encargado = models.CharField(max_length=80)
    NumEmpleados = models.IntegerField()
    Ubicacion = models.CharField(max_length=80)

    def __str__(self):
        return self.NombreSuc
