from rest_framework import serializers  # Importa el módulo de serialización de DRF
from django.contrib.auth import get_user_model  # Permite obtener el modelo de usuario activo en el proyecto

# Obtiene el modelo de usuario definido en models.py
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):  # Se extiende de ModelSerializer para automatizar el proceso de serialización
    class Meta:
        model = User  # Se usa el modelo de usuario personalizado
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password']  # Campos que se incluirán en la serialización
        extra_kwargs = {'password': {'write_only': True}}  # Hace que la contraseña solo sea visible al escribirla (no se muestra en respuestas)

    def create(self, validated_data):  # Sobreescribe el método para personalizar la creación del usuario
        """
        Este método se encarga de crear un nuevo usuario en la base de datos.
        Se usa `create_user()` en lugar de `create()` porque `create_user()` 
        maneja correctamente el hash de la contraseña.
        """
        user = User.objects.create_user(
            username=validated_data['username'],  # Asigna el nombre de usuario
            email=validated_data['email'],  # Asigna el email
            phone_number=validated_data.get('phone_number', ''),  # Asigna el número de teléfono si se proporciona, sino lo deja vacío
            role=validated_data.get('role', 'user'),  # Asigna el rol, si no se proporciona usa 'user' por defecto
            password=validated_data['password']  # Se asigna la contraseña, `create_user` la encripta automáticamente
        )
        return user  # Devuelve el usuario creado


