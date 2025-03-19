from rest_framework import generics, permissions
from .models import Producto
from .serializers import ProductoSerializer

class IsAdminUser(permissions.BasePermission):
    """Permiso personalizado para permitir solo a administradores acceder."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUser]  # Solo admins pueden acceder
