from django.db import models

# Create your models here.

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción del producto')

    def __str__(self):
        return self.nombre
