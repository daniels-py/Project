from django.urls import path, include  # Importamos la función path para definir las rutas
from rest_framework.routers import DefaultRouter  # Importamos el enrutador de DRF
from .views import ProductoListCreateView, ColorListCreateView


router = DefaultRouter()
# Registramos la vista ProductoListCreateView en el enrutador
router.register(r'productos', ProductoListCreateView, basename='productos')
router.register(r'carta-color', ColorListCreateView, basename='carta-color')
# Definimos las rutas de la API
urlpatterns = [
    path('', include(router.urls)),  # Incluimos las rutas de la API
]
