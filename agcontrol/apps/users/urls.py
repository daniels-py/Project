from django.urls import path  # Importamos la función path para definir las rutas
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # Importamos las vistas para el manejo de JWT
from .views import RegisterView, ProfileView, listUsers  # Importamos nuestras vistas personalizadas

# Definimos las rutas de la API
urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),  #  Ruta para registrar usuarios
    path('api/profile/', ProfileView.as_view(), name='profile'),  #  Ruta para ver el perfil del usuario autenticado

    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  #  Ruta para obtener tokens de acceso y refresco (Login)
    path('api/auth/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),  #  Ruta para refrescar el token de acceso
    path('api/users/', listUsers.as_view(), name='list_users'), # Ruta para listar usuarios sin necesidad de estar autentificado 
]
