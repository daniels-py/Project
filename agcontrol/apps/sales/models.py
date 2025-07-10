from django.db import models
from django.conf import settings  # Para relacionar con el modelo User personalizado
from apps.products.models import Producto, CaracteristicaColor
from apps.inventory.models import Inventario

# mejorar y destilar para ver quien genera la venta

class Venta(models.Model):  # Corregido: nombre del modelo con mayúscula inicial
    # Relación con el usuario que realizó la venta (admin o futuro usuario normal)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='ventas'
    )

    # registramos la fecha de la venta de forma automatica
    fecha = models.DateField(auto_now_add=True)

    metodo_pago = models.CharField(  # Corregido: 'charField' → 'CharField'
        max_length=50,
        choices=[
            ('efectivo', 'Efectivo'),
            ('digital', 'Pago Digital'),
        ],
        default='efectivo'
    )
    # espesificamos el tipo de pago que se realizo y podemos meter mas opciones

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # suma de los subtotales de los detalles de venta

    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # el mondo del cliente entrego o pago

    cambio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # la diferencia entre el total y lo que el cliente pago

    def calcular_totales(self):  # Corregido: 'calular_totales' → 'calcular_totales'
        # Calcula la suma de los subtotales de todos los detalles asociados a esta venta
        subtotal = sum([detalle.subtotal for detalle in self.detalles.all()])  # Corregido: self.detalle → self.detalles
        # Asigna el subtotal calculado al campo subtotal de la venta
        self.subtotal = subtotal
        # Calcula el cambio a devolver al cliente, asegurando que no sea negativo
        self.cambio = max(self.total_pagado - subtotal, 0)
        # Guarda los cambios en la base de datos
        self.save()

    def __str__(self):
        # Devuelve una representación legible de la venta
        return f"Venta #{self.id} - {self.metodo_pago} - {self.fecha.strftime('%Y-%m-%d')}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    # Relación con la tabla Venta (muchos detalles pueden pertenecer a una venta)
    # Si se borra la venta, se borran todos sus detalles automáticamente (CASCADE)
    # Se puede acceder así: venta.detalles.all()

    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    # Relación con Producto (el producto vendido)
    # Si el producto está asociado a una venta, no se puede eliminar (PROTECT)

    color = models.ForeignKey(CaracteristicaColor, on_delete=models.SET_NULL, null=True, blank=True)
    # Si el producto tiene color, se guarda el color específico
    # Si se elimina el color, se pone en NULL
    # Es opcional (null=True, blank=True)

    cantidad = models.PositiveIntegerField()
    # Cantidad de unidades vendidas

    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    # Precio que se cobró por una unidad del producto en el momento de la venta

    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    # Resultado de cantidad * precio_unitario (se calcula automáticamente al guardar)

    def save(self, *args, **kwargs):
        # Verifica si el color es obligatorio según el tipo de producto
        if self.producto.es_coloreable and not self.color:
            raise ValueError("Este producto requiere un color.")
        if not self.producto.es_coloreable and self.color:
            raise ValueError("Este producto no debe tener color.")

        # Calcula el subtotal
        self.subtotal = self.cantidad * self.precio_unitario

        # Busca el inventario exacto (producto + color si aplica)
        inventario_qs = Inventario.objects.filter(producto=self.producto, color=self.color)
        if not inventario_qs.exists():
            raise ValueError("No hay inventario disponible para este producto.")

        inventario = inventario_qs.first()
        if inventario.unidades < self.cantidad:
            raise ValueError("Stock insuficiente.")

        # Descuenta la cantidad vendida del inventario
        inventario.unidades -= self.cantidad
        inventario.save()

        # Guarda el detalle de venta
        super().save(*args, **kwargs)

    def __str__(self):
        # Muestra algo como: "Shampoo X x 3" o "Tinte 5.1 - Rubio Claro x 2"
        color = f" - {self.color.descripcion}" if self.color else ""
        return f"{self.producto.nombre}{color} x {self.cantidad}"

