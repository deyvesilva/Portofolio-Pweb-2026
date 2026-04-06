from django.contrib import admin
from .models import Experiencia

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cargo', 'descricao')
    search_fields = ('empresa', 'cargo')

    fieldsets = (
        ('Experiência', {
            'fields': ('empresa', 'cargo', 'descricao', 'data_inicio', 'data_fim')
        }),
    )