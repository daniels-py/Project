from django.urls import path
from .views import listMarca, listCategoria, listPresentacion

urlpatterns = [
    path('marca/', listMarca.as_view(), name='marca'),
    path('categoria/', listCategoria.as_view(), name='categoria'),
    path('presentacion/',listPresentacion.as_view(), name='presentacion')
]
