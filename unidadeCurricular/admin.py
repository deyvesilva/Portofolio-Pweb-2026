from django.contrib import admin
from .models import UnidadeCurricular

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'licenciatura')
    search_fields = ('nome',)
    list_filter = ('ano', 'semestre', 'licenciatura')