from rest_framework import serializers
from .models import Venta, DetalleVenta
from apps.products.models import Producto, CaracteristicaColor


class DetalleVentaSerializer(serializers.ModelSerializer):
    producto_id = serializers.IntegerField()
    color_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = DetalleVenta
        fields = ['producto_id', 'color_id', 'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['subtotal']


class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Venta
        fields = ['id', 'usuario', 'fecha', 'metodo_pago', 'subtotal', 'total_pagado', 'cambio', 'detalles']
        read_only_fields = ['id', 'fecha', 'subtotal', 'cambio']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        venta = Venta.objects.create(**validated_data)

        for detalle_data in detalles_data:
            producto = Producto.objects.get(id=detalle_data['producto_id'])
            color = None
            if producto.es_coloreable:
                color_id = detalle_data.get('color_id')
                if not color_id:
                    raise serializers.ValidationError("Este producto requiere un color.")
                color = CaracteristicaColor.objects.get(id=color_id)
            elif detalle_data.get('color_id'):
                raise serializers.ValidationError("Este producto no debe tener color.")

            detalle = DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                color=color,
                cantidad=detalle_data['cantidad'],
                precio_unitario=detalle_data['precio_unitario'],
                subtotal=detalle_data['cantidad'] * detalle_data['precio_unitario']
            )

        venta.calcular_totales()
        return venta
