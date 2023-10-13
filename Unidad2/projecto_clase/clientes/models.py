from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Cliente ID {self.id}, Nombre {self.nombre}, Correo: {self.correo}"