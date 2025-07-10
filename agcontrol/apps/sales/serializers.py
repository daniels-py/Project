from rest_framework import serializers
from .models import venta, DetalleVenta


# ajuste de logica de negocio para la venta 



class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = '__all__'  # Incluye todos los campos del modelo
        read_only_fields = ['fecha']  # Fecha se establece automáticamente al crear la venta


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'  # Incluye todos los campos del modelo

