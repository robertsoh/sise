from django.db import models


class Facultad(models.Model):
    nombre = models.CharField(max_length=254)
    codigo = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Facultades'

    def __str__(self):
        return self.nombre


class EAP(models.Model):
    nombre = models.CharField(max_length=254)
    codigo = models.CharField(max_length=20)
    facultad = models.ForeignKey(Facultad, related_name='eaps')

    def __str__(self):
        return self.nombre
