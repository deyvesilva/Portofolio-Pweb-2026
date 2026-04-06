from django.contrib import admin
from .models import Experiencia

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'cargo', 'data_inicio', 'data_fim', 'perfil')
    search_fields = ('empresa', 'cargo')
    list_filter = ('perfil',)
    ordering = ('-data_inicio',)

    filter_horizontal = ('tecnologias', 'competencias')

    fieldsets = (
        ('Experiência', {
            'fields': ('empresa', 'cargo', 'descricao', 'data_inicio', 'data_fim')
        }),
        ('Relacionamentos', {
            'fields': ('perfil', 'tecnologias', 'competencias')
        }),
    )