from django.contrib import admin
from .models import Competencia

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)