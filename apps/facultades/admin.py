from django.contrib import admin

from apps.facultades.models import Facultad, EAP


@admin.register(Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')


@admin.register(EAP)
class EAPdAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'facultad')
