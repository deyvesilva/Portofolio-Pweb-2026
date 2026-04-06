from django.contrib import admin
from .models import Licenciatura

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'universidade', 'ver_descricao')

    search_fields = ('nome', 'universidade')
    list_filter = ('universidade',)

    def ver_descricao(self, obj):
        return obj.descricao

    ver_descricao.short_description = 'Descrição'