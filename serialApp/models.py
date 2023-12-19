from unittest.util import _MAX_LENGTH
from django.db import models


class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.IntegerField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Inscritos(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fechaInscripcion = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    horaInscripcion = models.CharField(max_length=10)
      
    ESTADOS = (
        ('RESERVADO', 'RESERVADO'),
        ('COMPLETADA', 'COMPLETADA'),
        ('ANULADA', 'ANULADA'),
        ('NO ASISTEN', 'NO ASISTEN'),
    )
    estado = models.CharField(max_length=15, choices=ESTADOS, default='RESERVADO', blank=True, null=True,)
    observacion = models.CharField(max_length=150, null=True)  

class DatosAutor(models.Model):
    nombre = models.CharField(null=True, max_length=50)
    rut = models.CharField(null=True, max_length=50)