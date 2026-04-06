
from django.contrib import admin
from django.utils.html import format_html
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim','mostrar_logo')

    def mostrar_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80"/>', obj.logo.url)
        return "Sem logo"

    mostrar_logo.short_description = "Logo"