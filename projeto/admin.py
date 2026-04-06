from django.contrib import admin
from django.utils.html import format_html
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim', 'mostrar_imagem')

    readonly_fields = ('mostrar_imagem',)

    fieldsets = (
        ('Projeto', {
            'fields': ('nome', 'descricao', 'data_inicio', 'data_fim', 'github', 'imagem', 'mostrar_imagem')
        }),
    )

    def mostrar_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="100"/>', obj.imagem.url)
        return "-"

    mostrar_imagem.short_description = "Imagem"