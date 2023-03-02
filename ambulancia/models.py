from django.db import models

class Ambulancia(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    patente = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return f"{self.modelo} - {self.patente}"
