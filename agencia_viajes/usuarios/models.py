from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):  # Extiende el modelo de usuario de Django
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
