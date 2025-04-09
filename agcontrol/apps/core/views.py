from django.shortcuts import render
from .models import Marca,Categoria, Presentacion
from rest_framework import generics, permissions  # Importamos clases genéricas de DRF y permisos para la API
from .serializers import MarcaSerializer, CategoriaSerializer, PresentacionSerializer # Importamos el serializador del usuario
from rest_framework.permissions import BasePermission # esto es para crear permisos personalizados
from rest_framework.exceptions import PermissionDenied


# clase para validar mi permiso personalizado

class IsAdminUser(BasePermission):
    """Permiso personalizado para permitir solo a administradores acceder."""
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied(detail="Debes iniciar sesión para acceder a esta área.")

        if request.user.role != 'admin':
            raise PermissionDenied(detail="No tienes permitido el acceso a esta área.")

        return True  



class listMarca(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAdminUser]


class listCategoria(generics.ListCreateAPIView):
    queryset = Categoria.objects. all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]

class listPresentacion(generics.ListCreateAPIView):
    queryset = Presentacion.objects. all()
    serializer_class = PresentacionSerializer
    permission_classes =  [IsAdminUser]