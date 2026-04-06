from django.contrib import admin
from .models import Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'uc')
    search_fields = ('nome',)
    list_filter = ('uc', 'data')