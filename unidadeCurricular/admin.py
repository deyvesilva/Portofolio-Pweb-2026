from django.contrib import admin
from django.utils.html import format_html
from .models import UnidadeCurricular

@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'mostrar_imagem')

    readonly_fields = ('mostrar_imagem',)

    fieldsets = (
        ('UC', {
            'fields': ('nome', 'descricao', 'imagem', 'mostrar_imagem', 'ano', 'semestre')
        }),
    )

    def mostrar_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="100"/>', obj.imagem.url)
        return "-"

    mostrar_imagem.short_description = "Imagem"