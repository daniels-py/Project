from rest_framework import viewsets
from .models import venta, DetalleVenta
from .serializers import ventaSerializer, DetalleVentaSerializer

# Create your views here.


class ventaListCreateView(viewsets.ModelViewSet):
    queryset = venta.objects.all()
    serializer_class = ventaSerializer

class DetalleVentaListCreateView(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer

    def perform_create(self, serializer):
        # Aquí puedes agregar lógica adicional antes de guardar el detalle de la venta
        serializer.save()  # Guarda el detalle de la venta