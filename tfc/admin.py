from django.contrib import admin
from django.utils.html import format_html
from .models import TFC

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao','rating')


    fieldsets = (
        ('TFC', {
            'fields': ('titulo', 'descricao', 'rating')
        }),
    )

    