from django.db import models
from apps.core.models import *

# Create your models here.



class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción del producto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    codigo = models.CharField(max_length=100, unique=True, null=True, blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT)

    es_coloreable = models.BooleanField(default=False)
    
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.marca.nombre}"




class CaracteristicaColor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='colores')
    codigo_color = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.producto.marca} - {self.producto.nombre} - {self.descripcion} - {self.codigo_color}"

