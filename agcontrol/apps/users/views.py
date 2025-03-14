from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

User = get_user_model()

#  Vista para Registrar un Usuario
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Cualquier persona puede registrarse


#  Vista para Ver el Perfil del Usuario Autenticado
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados

    def get(self, request):
        user = request.user
        return Response({
            "message": f"¡Bienvenido, {user.username}!",  # Mensaje de bienvenida
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'role': user.role
        })
