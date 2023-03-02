from django.db import models

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    estado = models.CharField(
        max_length=20,
        choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('vacaciones', 'De vacaciones'), ('enfermo', 'Enfermo')],
        default='activo'
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.dni}"

class Tens(Personal):
    pass

class Chofer(Personal):
    pass

class Administrativo(Personal):
    pass
