from django.contrib import admin
from .models import Formacao

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'entidade', 'descricao')

    search_fields = ('nome', 'entidade')

    fieldsets = (
        ('Formação', {
            'fields': ('nome', 'entidade', 'descricao', 'data')
        }),
    )