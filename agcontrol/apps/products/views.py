from rest_framework import viewsets
from .models import Producto ,CaracteristicaColor
from .serializers import ProductoSerializer, ColorSerializer
from permissions.permissions import IsAdminUser  # Aquí mi permios personalizado


class ProductoListCreateView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ColorListCreateView(viewsets.ModelViewSet):
    queryset = CaracteristicaColor.objects.all()
    serializer_class = ColorSerializer
    