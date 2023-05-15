from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=60)
    Correo = models.EmailField(max_length = 254)
    TipoCliente = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre
