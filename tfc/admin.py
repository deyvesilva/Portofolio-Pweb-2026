from django.contrib import admin
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano')
    search_fields = ('titulo',)
    list_filter = ('ano',)
    ordering = ('-ano',)

    filter_horizontal = ('tecnologias',)

    fieldsets = (
        ('TFC', {
            'fields': ('titulo', 'descricao', 'ano', 'link')
        }),
        ('Tecnologias', {
            'fields': ('tecnologias',)
        }),
    )