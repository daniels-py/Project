from .models import Marca,Categoria, Presentacion
from rest_framework import viewsets  # Importamos clases genéricas de DRF y permisos para la API
from .serializers import MarcaSerializer, CategoriaSerializer, PresentacionSerializer # Importamos el serializador del usuario
from permissions.permissions import IsAdminUser  # mi permiso personalizado


class listMarca(viewsets.ModelViewSet):  
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAdminUser]


class listCategoria(viewsets.ModelViewSet):
    queryset = Categoria.objects. all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUser]

class listPresentacion(viewsets.ModelViewSet):

    queryset = Presentacion.objects. all()
    serializer_class = PresentacionSerializer
    permission_classes =  [IsAdminUser]