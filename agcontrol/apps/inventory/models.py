from django.db import models
from agcontrol.apps.products.models import Producto

# Create your models here.


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='inventario')
    unidades = models.PositiveIntegerField(default=0, verbose_name='Unidades en inventario')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    def __str__(self):
        return f"{self.producto.nombre} - Stock: {self.unidades}"