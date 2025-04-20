from django.shortcuts import render
from .models import Inventario
from rest_framework import generics, permissions
from .serializers import InventarioSerializer
from permissions.permissions import IsAdminUser # mi permiso personalizado


class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAdminUser]