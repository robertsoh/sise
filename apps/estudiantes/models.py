from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from apps.facultades.models import EAP
from apps.ubigeo.models import Departamento, Provincia, Distrito


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
    direccion_provincia = ChainedForeignKey(
        Provincia,
        chained_field="direccion_departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True,
        sort=True)
    direccion_distrito = ChainedForeignKey(
        Distrito,
        chained_field="direccion_provincia",
        chained_model_field="provincia",
        show_all=False,
        auto_choose=True,
        sort=True)
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
