from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import * 
from .forms import *

def home_view(request):
    return render(request, 'portfolio/home.html')

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all().order_by('-nivel')
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})

def licenciatura_view(request):
    licenciatura = Licenciatura.objects.first()
    ucs = UnidadeCurricular.objects.filter(licenciatura=licenciatura).order_by('ano', 'semestre')
    return render(request, 'portfolio/licenciatura.html', {'licenciatura': licenciatura, 'ucs': ucs})

def projetos_view(request):
    projetos = Projeto.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})

def tfc_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfc.html', {'tfcs': tfcs})

def curriculo_view(request):
    perfil = Perfil.objects.first()
    exp = Experiencia.objects.all()
    form = Formacao.objects.all()
    comp = Competencia.objects.all()
    return render(request, 'portfolio/curriculo.html', {'perfil': perfil, 'experiencias': exp, 'formacoes': form, 'competencias': comp})

def tfc_view(request):
    tfcs = TFC.objects.all()
    return render(request, 'portfolio/tfc.html', {'tfcs': tfcs})


# CRUD DE TODOS OS MODELS.PY

# --- PROJETOS ---
class ProjetoCreateView(CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('projetos')

class ProjetoUpdateView(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('projetos')

class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('projetos')

# --- TFC ---
class TFCCreateView(CreateView):
    model = TFC
    form_class = TFCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('tfc')

class TFCUpdateView(UpdateView):
    model = TFC
    form_class = TFCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('tfc')

class TFCDeleteView(DeleteView):
    model = TFC
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('tfc')

# --- LICENCIATURA E UCs ---
class LicenciaturaUpdateView(UpdateView):
    model = Licenciatura
    form_class = LicenciaturaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('licenciatura')

class UCCreateView(CreateView):
    model = UnidadeCurricular
    form_class = UCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('licenciatura')

class UCUpdateView(UpdateView):
    model = UnidadeCurricular
    form_class = UCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('licenciatura')

class UCDeleteView(DeleteView):
    model = UnidadeCurricular
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('licenciatura')

# --- CURRÍCULO (Perfil, Experiência, Formação) ---
class PerfilUpdateView(UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('curriculo')

class ExperienciaCreateView(CreateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('curriculo')

class ExperienciaUpdateView(UpdateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('curriculo')

class ExperienciaDeleteView(DeleteView):
    model = Experiencia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('curriculo')

# --- TECNOLOGIAS ---
class TecnologiaCreateView(CreateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('tecnologias')

class TecnologiaUpdateView(UpdateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('tecnologias')

class TecnologiaDeleteView(DeleteView):
    model = Tecnologia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('tecnologias')
    
    # --- CRUD COMPETÊNCIAS ---
class CompetenciaCreateView(CreateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('dashboard')

class CompetenciaUpdateView(UpdateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('dashboard')

class CompetenciaDeleteView(DeleteView):
    model = Competencia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
    
def dashboard_view(request):
    context = {
        'perfil': Perfil.objects.first(),
        'licenciatura': Licenciatura.objects.first(),
        'projetos': Projeto.objects.all(),
        'ucs': UnidadeCurricular.objects.all(),
        'tecnologias': Tecnologia.objects.all(),
        'tfcs': TFC.objects.all(),
        'experiencias': Experiencia.objects.all(),
        'competencias': Competencia.objects.all(),
        'formacoes': Formacao.objects.all(),

    }
    return render(request, 'portfolio/dashboard.html', context)