from rest_framework import serializers
from .models import Producto, CaracteristicaColor

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # Incluye todos los campos del modelo


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicaColor
        fields = '__all__' 


