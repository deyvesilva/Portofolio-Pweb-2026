from django.contrib import admin
from .models import MakingOf

@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('id', 'projeto')
    search_fields = ('descricao',)
    list_filter = ('projeto',)

    fieldsets = (
        ('Registo', {
            'fields': ('registos',)
        }),
        ('Reflexão', {
            'fields': ('decisoes', 'erros', 'justificacoes', 'uso_ia')
        }),
        ('Ligação', {
            'fields': ('projeto',)
        }),
    )