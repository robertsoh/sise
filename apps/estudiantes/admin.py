from django.contrib import admin

from apps.estudiantes.models import Estudiante, EstudianteEAP, Grado


@admin.register(Estudiante)
class EstudiantedAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'correo')

    class Media:
        js = (
            'smart-selects/admin/js/chainedfk.js',
            'smart-selects/admin/js/chainedm2m.js',
            'smart-selects/admin/js/bindfields.js',
        )


@admin.register(EstudianteEAP)
class EstudianteEAPAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'eap', 'fecha_inicio', 'fecha_fin')


@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')





