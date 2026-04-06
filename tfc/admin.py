from django.contrib import admin
from django.utils.html import format_html
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'rating', 'mostrar_imagem')

    readonly_fields = ('mostrar_imagem',)

    fieldsets = (
        ('TFC', {
            'fields': ('titulo', 'descricao', 'ano', 'rating', 'imagem', 'mostrar_imagem')
        }),
    )

    def mostrar_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="100"/>', obj.imagem.url)
        return "-"

    mostrar_imagem.short_description = "Imagem"