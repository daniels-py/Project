from django.db import models

# Create your models here.

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción del producto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    codigo = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nombre

