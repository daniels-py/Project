from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    email= models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'  # Define el campo que se usará para iniciar sesión
    REQUIRED_FIELDS = ['username']  # Campos requeridos al crear un usuario

    def __str__(self):
        return f"{self.username} - {self.email}"
    
    