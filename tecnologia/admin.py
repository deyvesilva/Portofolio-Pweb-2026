from django.contrib import admin
from .models import Tecnologia

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nivel')
    search_fields = ('nome',)
    list_filter = ('nivel',)
    ordering = ('nome',)

    fieldsets = (
        ('Tecnologia', {
            'fields': ('nome', 'descricao', 'website', 'logo', 'nivel')
        }),
    )