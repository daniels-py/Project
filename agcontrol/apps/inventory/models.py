from django.db import models
from apps.products.models import *

# Create your models here.

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario')
    color = models.ForeignKey(CaracteristicaColor, on_delete=models.SET_NULL, null=True, blank=True)
    unidades = models.PositiveIntegerField(default=0)

    def __str__(self):
        color_info = f" - {self.color.descripcion}" if self.color else ""
        return f"{self.producto.nombre}{color_info} - Stock: {self.unidades}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.producto.es_coloreable and not self.color:
            raise ValidationError("Este producto requiere un color.")
        if not self.producto.es_coloreable and self.color:
            raise ValidationError("Este producto no debería tener un color.")