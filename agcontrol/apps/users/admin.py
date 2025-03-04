from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Importamos la clase UserAdmin para extenderla
from .models import User  # Importamos nuestro modelo personalizado de usuario

# Definimos una clase personalizada para el panel de administración de usuarios
class CustomUserAdmin(UserAdmin):
    model = User  # Especificamos que este administrador maneja el modelo User

    # list_display: Define qué campos se mostrarán en la lista de usuarios en el admin
    list_display = ('username', 'email', 'phone_number', 'role', 'is_staff', 'is_active')

    # list_filter: Agrega filtros laterales en el admin para facilitar la búsqueda de usuarios
    list_filter = ('role', 'is_staff', 'is_active')

    # fieldsets: Define la estructura de los campos al visualizar/editar un usuario en el admin
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),  # Campos básicos
        ('Personal Info', {'fields': ('phone_number',)}),  # Sección para la info personal
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'groups', 'user_permissions')}),  # Permisos y roles
        ('Important dates', {'fields': ('last_login', 'date_joined')}),  # Fechas clave del usuario
    )

    # add_fieldsets: Define los campos mostrados al agregar un nuevo usuario desde el admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # Clase CSS para que los campos sean más anchos
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'role', 'is_staff', 'is_active')}
        ),
    )

    # search_fields: Define en qué campos se puede buscar en el admin
    search_fields = ('email', 'username')

    # ordering: Especifica el orden en el que se muestran los usuarios (por email en este caso)
    ordering = ('email',)

# Registramos el modelo en el panel de administración usando nuestra clase personalizada
admin.site.register(User, CustomUserAdmin)
