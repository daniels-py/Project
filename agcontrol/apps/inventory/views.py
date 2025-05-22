from .models import Inventario
from rest_framework import viewsets
from .serializers import InventarioSerializer
from permissions.permissions import IsAdminUser # mi permiso personalizado


class InventarioList(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAdminUser]