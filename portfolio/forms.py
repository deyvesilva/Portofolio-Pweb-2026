from django import forms
from .models import *

class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = '__all__'

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

class UCForm(forms.ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = '__all__'

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = '__all__'

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'

class TFCForm(forms.ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'

class MakingOfForm(forms.ModelForm):
    class Meta:
        model = MakingOf
        fields = '__all__'