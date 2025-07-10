from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ventaListCreateView, DetalleVentaListCreateView

router = DefaultRouter()
router.register(r'ventas', ventaListCreateView, basename='ventas')
router.register(r'detalle-ventas', DetalleVentaListCreateView, basename='detalle-')

urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas de la API
]