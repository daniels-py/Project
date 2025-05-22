from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from permissions.permissions import IsAdminUser  # Aquí mi permios personalizado


class ProductoListCreateView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUser]  # Solo admins pueden acceder
