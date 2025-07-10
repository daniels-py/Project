from django.urls import path
from .views import CrearVentaView, MisVentasView

urlpatterns = [
    path('crear/', CrearVentaView.as_view(), name='crear_venta'),         # POST para crear una venta
    path('mis-ventas/', MisVentasView.as_view(), name='mis_ventas'),      # GET para listar mis ventas
]
