from django.contrib import admin
from .models import Formacao

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'entidade', 'data')
    search_fields = ('nome', 'entidade')
    list_filter = ('entidade',)
    ordering = ('-data',)

    filter_horizontal = ('competencias',)

    fieldsets = (
        ('Formação', {
            'fields': ('nome', 'entidade', 'descricao', 'data')
        }),
        ('Relacionamentos', {
            'fields': ('perfil', 'competencias')
        }),
    )