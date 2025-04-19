from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  # Campo adicional para confirmar la contraseña

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'role', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Verifica que las dos contraseñas coincidan.
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return data

    def create(self, validated_data):
        # Quitamos password2 ya que no se usa en la creación del usuario
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', ''),
            role=validated_data.get('role', 'user'),
            password=validated_data['password']
        )
        return user
