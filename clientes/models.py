from django.db import models

class Consulta(models.Model):
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    detalle = models.TextField(blank=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"