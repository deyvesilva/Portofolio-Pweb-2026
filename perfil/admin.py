from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'bio_resumida')
    search_fields = ('nome',)
    list_filter = ('idade',)
    ordering = ('nome',)

    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'idade', 'bio')
        }),
    )

    def bio_resumida(self, obj):
        if obj.bio:
            return (obj.bio[:50] + '...') if len(obj.bio) > 50 else obj.bio
        return "-"

    bio_resumida.short_description = 'Bio'