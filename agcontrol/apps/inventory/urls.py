from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventarioList


router = DefaultRouter()
router.register(r'inventario', InventarioList, basename='inventario')

urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas de la API
]