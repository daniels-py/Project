from rest_framework import serializers
from .models import venta, DetalleVenta

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ['fecha']  # Fecha se establece automáticamente al crear la venta


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'  # Incluye todos los campos del modelo

