from django.contrib import admin
from .models import Producto  # Importamos el modelo Producto

# Register your models here.

admin.site.register(Producto)  # Registramos el modelo en el panel de administración
