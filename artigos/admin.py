from django.contrib import admin
from .models import Artigo, Comentario

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao')
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk: # Se for um novo artigo
            obj.autor = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Comentario)