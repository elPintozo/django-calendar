from django.db import models

from ambulancia.models import Ambulancia
from personal.models import Personal, Tens, Chofer

class Asignacion(models.Model):
    ambulancia = models.ForeignKey(Ambulancia, on_delete=models.PROTECT)
    chofer = models.ForeignKey(Chofer, on_delete=models.PROTECT)
    tens = models.ManyToManyField(Tens, related_name='asignaciones')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f"{self.ambulancia.nombre} - {self.fecha_inicio}"

class HorarioLaboral(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.PROTECT)
    horas_trabajadas = models.PositiveIntegerField(default=0)
    horas_vacaciones = models.PositiveIntegerField(default=0)
    horas_ausencias = models.PositiveIntegerField(default=0)
    horas_permitidas_trabajadas = models.PositiveIntegerField(default=0)
    horas_permitidas_vacaciones = models.PositiveIntegerField(default=0)
    horas_permitidas_ausencias = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.personal} - Horario Laboral"