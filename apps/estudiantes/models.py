from django.db import models
from ubigeo.models import Departamento, Provincia, Distrito

from apps.facultades.models import EAP


class Grado(models.Model):
    nombre = models.CharField(max_length=254)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):

    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    direccion_departamento = models.ForeignKey(Departamento)
    direccion_provincia = models.ForeignKey(Provincia)
    direccion_distrito = models.ForeignKey(Distrito)
    direccion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField(max_length=254)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellido_paterno, self.apellido_materno)


class EstudianteEAP(models.Model):
    eap = models.ForeignKey(EAP)
    estudiante = models.ForeignKey(Estudiante, related_name='estudiante_eaps')
    fecha_inicio = models.DateField('Fecha inicio')
    fecha_fin = models.DateField('Fecha fin', blank=True, null=True)


class EstudianteGrado(models.Model):
    estudiante = models.ForeignKey(Estudiante, related_name='estudiante_grados')
    grado = models.ForeignKey(Grado, related_name='+')
    fecha = models.DateField()
