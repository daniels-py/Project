from django.urls import path
from .views import InventarioList

urlpatterns = [
    path('inventario/', InventarioList.as_view(), name='inventario'),
]
