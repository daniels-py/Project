from django.db import models
from apps.products.models import Producto, CaracteristicaColor
from apps.inventory.models import Inventario


# mejorar y destilar para ver quien genera la venta


class venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    total  = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"venta {self.id} - {self.fecha.strftime('%d/%m/%Y')} - Total: {self.total}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(venta, on_delete=models.CASCADE, related_name='detalle')
    Producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    color = models.ForeignKey(CaracteristicaColor, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,)

    def save(self, *args, **kwargs):
        # Validación de color según el producto
        if self.producto.es_coloreable and not self.color:
            raise ValueError("Este producto requiere un color.")
        if not self.producto.es_coloreable and self.color:
            raise ValueError("Este producto no debe tener color.")

        self.subtotal = self.cantidad * self.precio_unitario

        # Buscar inventario
        inventario_qs = Inventario.objects.filter(producto=self.producto, color=self.color)
        if not inventario_qs.exists():
            raise ValueError("No hay inventario para este producto/color.")

        inventario = inventario_qs.first()
        if inventario.unidades < self.cantidad:
            raise ValueError("Stock insuficiente para este producto.")

        # Descontar unidades
        inventario.unidades -= self.cantidad
        inventario.save()

        super().save(*args, **kwargs)

    def __str__(self):
        color = f" - {self.color.descripcion}" if self.color else ""
        return f"{self.producto.nombre}{color} x {self.cantidad}"
