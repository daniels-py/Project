from rest_framework import generics, permissions
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.permissions import BasePermission # esto es para crear permisos personalizados
from rest_framework.exceptions import PermissionDenied

class IsAdminUser(BasePermission):
    """Permiso personalizado para permitir solo a administradores acceder."""
    
    def has_permission(self, request, view):
        # se generan 2 condiciones conde si el usuario no esta utentificado no podra ingresar
        if not request.user.is_authenticated:
            # permision es un excepcion que se lanza cuando para enviar un mcodigo de error 403
            # en este caso se envia un mensaje de error perzonalizados 
            raise PermissionDenied(detail="Debes iniciar sesión para acceder a esta área.")

        if request.user.role != 'admin':
             # porque no retur porque lo maneja de forma generica 
            # en cambio raise es para lanzar una excepcion a nuestra respuesta 403
            raise PermissionDenied(detail="No tienes permitido el acceso a esta área.")

        return True  # Permite el acceso solo si es admin


class ProductoListCreateView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUser]  # Solo admins pueden acceder
