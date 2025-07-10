from rest_framework import generics, permissions
from .models import Venta
from .serializers import VentaSerializer
from permissions.permissions import IsAdminUser  # mi permiso personalizado



# Crear una venta con sus detalles
class CrearVentaView(generics.CreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAdminUser]


    def perform_create(self, serializer):
        # Asigna automáticamente el usuario que hace la venta
        serializer.save(usuario=self.request.user)


# Listar las ventas realizadas por el usuario autenticado
class MisVentasView(generics.ListAPIView):
    serializer_class = VentaSerializer
    permission_classes = [IsAdminUser]



    def get_queryset(self):
        return Venta.objects.filter(usuario=self.request.user).order_by('-fecha')
