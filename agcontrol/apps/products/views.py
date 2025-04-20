from rest_framework import generics, permissions
from .models import Producto
from .serializers import ProductoSerializer
from permissions.permissions import IsAdminUser  # 👈 Aquí lo estás usando


class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUser]  # Solo admins pueden acceder
