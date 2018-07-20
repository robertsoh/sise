from django.contrib import admin

from apps.estudiantes.models import Estudiante, EstudianteEAP, Grado


@admin.register(Estudiante)
class EstudiantedAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'correo')


@admin.register(EstudianteEAP)
class EstudiantedAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'eap',)


@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')





