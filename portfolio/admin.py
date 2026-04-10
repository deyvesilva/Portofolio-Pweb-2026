from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Licenciatura, Perfil, Tecnologia, Competencia,
    UnidadeCurricular, Projeto, Experiencia,
    Formacao, TFC, MakingOf
)

# 🔹 Função reutilizável para mostrar imagens
def mostrar_imagem(obj, campo):
    imagem = getattr(obj, campo)
    if imagem:
        return format_html('<img src="{}" width="60" height="35" style="object-fit:cover;" />', imagem.url)
    return "Sem imagem"

list_display = ('nome', 'mostrar_logo','titulo','rating')


# =========================
# LICENCIATURA
# =========================
@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "universidade", "ver_descricao")
    search_fields = ("nome", "universidade")
    list_filter = ("universidade",)

    def ver_descricao(self, obj):
        return obj.descricao[:700] + "..." if len(obj.descricao) > 50 else obj.descricao

    ver_descricao.short_description = "Descrição"


# =========================
# PERFIL
# =========================
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "bio")
    search_fields = ("nome",)
    list_filter = ("idade",)


# =========================
# TECNOLOGIA
# =========================
@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel", "ver_descricao", "mostrar_logo")
    search_fields = ("nome",)
    list_filter = ("nivel",)

    def ver_descricao(self, obj):
        return obj.descricao[:300]

    def mostrar_logo(self, obj):
        return mostrar_imagem(obj, "logo")

    mostrar_logo.short_description = "Logo"


# =========================
# COMPETENCIA
# =========================
@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


# =========================
# UNIDADE CURRICULAR
# =========================
@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano", "semestre", "licenciatura", "mostrar_imagem", "ver_descricao")
    search_fields = ("nome",)
    list_filter = ("ano", "semestre", "licenciatura")

    def mostrar_imagem(self, obj):
        return mostrar_imagem(obj, "imagem")

    def ver_descricao(self, obj):
        return obj.descricao[0:]


# =========================
# PROJETO
# =========================
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = (
        "nome", "uc", "data_de_inicio", "data_de_fim",
        "mostrar_logo", "ver_descricao"
    )
    search_fields = ("nome",)
    list_filter = ("uc", "data_de_inicio")

    filter_horizontal = ("tecnologias", "competencias")

    def mostrar_logo(self, obj):
        return mostrar_imagem(obj, "logo")

    def ver_descricao(self, obj):
        return obj.descricao[:264]


# =========================
# EXPERIENCIA
# =========================
@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cargo", "data_de_inicio", "data_de_fim", "ver_descricao")
    search_fields = ("empresa", "cargo")
    list_filter = ("data_de_inicio",)

    filter_horizontal = ("tecnologias", "competencias")

    def ver_descricao(self, obj):
        return obj.descricao[:400]


# =========================
# FORMAÇÃO
# =========================
@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "entidade", "data_de_inicio","data_de_fim", "ver_descricao")
    search_fields = ("nome", "entidade")
    list_filter = ("data_de_inicio","data_de_fim")

    filter_horizontal = ("competencias",)

    def ver_descricao(self, obj):
        return obj.descricao[:500]


# =========================
# TFC
# =========================
@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "rating", "ver_descricao")
    search_fields = ("titulo",)
    list_filter = ("ano", "rating")

    filter_horizontal = ("tecnologias",)

    def ver_descricao(self, obj):
        return obj.descricao[:50]


# =========================
# MAKING OF
# =========================
@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("id", "projeto", "mostrar_imagem", "decisoes")
    search_fields = ("decisoes",)
    list_filter = ("projeto",)

    def mostrar_imagem(self, obj):
        return mostrar_imagem(obj, "registos")

    mostrar_imagem.short_description = "Registos"
    
    