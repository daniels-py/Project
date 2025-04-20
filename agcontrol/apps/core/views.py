from django.shortcuts import render
from .models import Marca,Categoria, Presentacion
from rest_framework import generics, permissions  # Importamos clases genéricas de DRF y permisos para la API
from .serializers import MarcaSerializer, CategoriaSerializer, PresentacionSerializer # Importamos el serializador del usuario
from permissions.permissions import IsAdminUser  # mi permiso personalizado


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