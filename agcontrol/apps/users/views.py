from rest_framework import status, generics, permissions  # Importamos clases genéricas de DRF y permisos para la API
from django.contrib.auth import get_user_model  # Obtiene el modelo de usuario activo en el proyecto
from rest_framework.response import Response  # Permite devolver respuestas JSON en las vistas
from rest_framework.views import APIView  # Se usa para crear vistas basadas en clases
from .serializers import UserSerializer  # Importamos el serializador del usuario
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailLoginTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


# Obtener el modelo de usuario definido en models.py
User = get_user_model()

#  Vista para Registrar un Usuario
class RegisterView(generics.CreateAPIView):  # Hereda de CreateAPIView, que se usa para crear registros
    queryset = User.objects.all()  # Define la consulta de usuarios existentes (requerido por CreateAPIView)
    serializer_class = UserSerializer  # Usa el serializador para validar y crear usuarios
    permission_classes = [permissions.AllowAny]  # Permite que cualquier persona acceda a esta vista (sin autenticación)

    """
     ¿Cómo funciona esta vista?
    - `CreateAPIView` maneja automáticamente el método POST para crear un nuevo usuario.
    - Se usa el `UserSerializer` para validar los datos y llamar al método `create()`.
    - Al no definir manualmente `post()`, Django REST Framework lo maneja automáticamente.
    """

# Vista para Ver el Perfil del Usuario Autenticado
class ProfileView(APIView):  # Hereda de APIView para definir una vista más personalizada
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request):  # Define el método GET para obtener los datos del usuario autenticado
        """
         ¿Qué hace este método?
        - Obtiene el usuario autenticado (`request.user`).
        - Devuelve los datos del usuario en formato JSON.
        - Agrega un mensaje de bienvenida personalizado.
        """
        user = request.user  # Obtiene el usuario que está haciendo la solicitud
        return Response({  # Retorna un JSON con los datos del usuario
            "message": f"¡Bienvenido, {user.username}!",  # Mensaje de bienvenida
            "id":  user.id,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'role': user.role
        })

class listUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista para el login personalizado
class EmailLoginView(TokenObtainPairView):
    serializer_class = EmailLoginTokenSerializer

# vista para el logout
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # creamos un metodo para el logout 
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            
            return Response({"detail": "Sesión cerrada correctamente."}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "No se proporcionó el token de actualización."}, status=status.HTTP_400_BAD_REQUEST)
        except (TokenError, InvalidToken):
            return Response({"error": "Token inválido o ya ha sido invalidado."}, status=status.HTTP_400_BAD_REQUEST)
       




class EmailLoginTokenSerializer(TokenObtainPairView):
    serializer_class = EmailLoginTokenSerializer

