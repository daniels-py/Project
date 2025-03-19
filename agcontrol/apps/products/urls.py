from django.urls import path
from .views import ProductoListCreateView

urlpatterns = [
    path('productos/', ProductoListCreateView.as_view(), name='productos'),
]
