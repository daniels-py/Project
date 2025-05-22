from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import listMarca, listCategoria, listPresentacion

routers = DefaultRouter()
routers.register(r'marca', listMarca, basename='marca')
routers.register(r'categoria', listCategoria, basename='categoria')
routers.register(r'presentacion', listPresentacion, basename='presentacion')

urlpatterns = [
    path('', include(routers.urls)),  # Incluimos las rutas de la API

]