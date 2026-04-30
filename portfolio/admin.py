from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Licenciatura, Perfil, Tecnologia, Competencia,
    UnidadeCurricular, Projeto, Experiencia,
    Formacao, TFC, MakingOf, TipoTecnologia
)

# Função auxiliar para exibir imagens no Admin
def mostrar_imagem(obj, campo_imagem):
    imagem = getattr(obj, campo_imagem, None)
    if imagem:
        return format_html('<img src="{}" width="50" height="50" style="object-fit: contain;" />', imagem.url)
    return "Sem imagem"

# =========================
# TIPO TECNOLOGIA
# =========================
@admin.register(TipoTecnologia)
class TipoTecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

# =========================
# TECNOLOGIA
# =========================
@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "nivel", "ver_descricao", "mostrar_logo")
    search_fields = ("nome",)
    list_filter = ("nivel", "tipo")

    def ver_descricao(self, obj):
        return obj.descricao[:300] if obj.descricao else ""

    def mostrar_logo(self, obj):
        return mostrar_imagem(obj, "logo")

    mostrar_logo.short_description = "Logo"

# =========================
# LICENCIATURA
# =========================
@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "universidade", "ver_descricao")
    search_fields = ("nome", "universidade")
    list_filter = ("universidade",)

    def ver_descricao(self, obj):
        if obj.descricao:
            return obj.descricao[:100] + "..." if len(obj.descricao) > 100 else obj.descricao
        return ""

    ver_descricao.short_description = "Descrição"

# =========================
# PERFIL
# =========================
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade", "bio")
    search_fields = ("nome",)

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
    list_display = ("nome", "ano", "semestre", "licenciatura", "exibir_imagem")
    search_fields = ("nome",)
    list_filter = ("ano", "semestre", "licenciatura")

    def exibir_imagem(self, obj):
        return mostrar_imagem(obj, "imagem")
    
    exibir_imagem.short_description = "Imagem"

# =========================
# PROJETO
# =========================
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("nome", "uc", "data_de_inicio", "mostrar_logo")
    search_fields = ("nome",)
    list_filter = ("uc", "data_de_inicio")
    filter_horizontal = ("tecnologias", "competencias")

    def mostrar_logo(self, obj):
        return mostrar_imagem(obj, "logo")

# =========================
# EXPERIENCIA
# =========================
@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("empresa", "cargo", "data_de_inicio")
    search_fields = ("empresa", "cargo")
    filter_horizontal = ("tecnologias", "competencias")

# =========================
# FORMAÇÃO
# =========================
@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "entidade", "data_de_inicio")
    search_fields = ("nome", "entidade")
    filter_horizontal = ("competencias",)

# =========================
# TFC
# =========================
@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ano", "rating", "exibir_capa")
    search_fields = ("titulo",)
    list_filter = ("ano", "rating")
    filter_horizontal = ("tecnologias",)
    
    def exibir_capa(self, obj):
        # TFC usa o campo 'imagem' conforme o teu código original
        return mostrar_imagem(obj, "imagem")
    
    exibir_capa.short_description = "Capa/Imagem"

# =========================
# MAKING OF
# =========================
@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("id", "exibir_registo", "decisoes", "uso_ia")
    search_fields = ("decisoes",)

    def exibir_registo(self, obj):
        return mostrar_imagem(obj, "registos")

    exibir_registo.short_description = "Registos"