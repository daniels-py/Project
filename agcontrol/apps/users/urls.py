from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),  # Registro de usuario
    path('api/profile/', ProfileView.as_view(), name='profile'),  # Ver perfil (requiere autenticación)

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login con JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token
]
