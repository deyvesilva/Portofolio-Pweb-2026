from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import * 
from .forms import *

# --- FUNÇÃO AUXILIAR DE PERMISSÃO ---
def is_gestor(user):
    """Verifica se o utilizador pertence ao grupo ou é superuser"""
    return user.groups.filter(name='gestor-portfolio').exists() or user.is_superuser

# --- VIEWS PÚBLICAS (Apenas Leitura) ---

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

def sobre_view(request):
    context = {
        'tipos_tecnologia': TipoTecnologia.objects.all(),
        'registos_making_of': MakingOf.objects.all().order_by('-id'),
    }
    return render(request, 'portfolio/sobre.html', context)

# --- DASHBOARD (Acesso apenas a utilizadores autenticados) ---
@login_required
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


# --- CRUD PROTEGIDO (Classes) ---
class GestorRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_gestor(self.request.user)

# --- PROJETOS ---
class ProjetoCreateView(GestorRequiredMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:projetos')

class ProjetoUpdateView(GestorRequiredMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:projetos')

class ProjetoDeleteView(GestorRequiredMixin, DeleteView):
    model = Projeto
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:projetos')

# --- TFC ---
class TFCCreateView(GestorRequiredMixin, CreateView):
    model = TFC
    form_class = TFCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:tfc')

class TFCUpdateView(GestorRequiredMixin, UpdateView):
    model = TFC
    form_class = TFCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:tfc')

class TFCDeleteView(GestorRequiredMixin, DeleteView):
    model = TFC
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:tfc')

# --- LICENCIATURA E UCs ---
class LicenciaturaUpdateView(GestorRequiredMixin, UpdateView):
    model = Licenciatura
    form_class = LicenciaturaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:licenciatura')

class UCCreateView(GestorRequiredMixin, CreateView):
    model = UnidadeCurricular
    form_class = UCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:licenciatura')

class UCUpdateView(GestorRequiredMixin, UpdateView):
    model = UnidadeCurricular
    form_class = UCForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:licenciatura')

class UCDeleteView(GestorRequiredMixin, DeleteView):
    model = UnidadeCurricular
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:licenciatura')

# --- CURRÍCULO ---
class PerfilUpdateView(GestorRequiredMixin, UpdateView):
    model = Perfil
    form_class = PerfilForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:curriculo')

class ExperienciaCreateView(GestorRequiredMixin, CreateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:curriculo')

class ExperienciaUpdateView(GestorRequiredMixin, UpdateView):
    model = Experiencia
    form_class = ExperienciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:curriculo')

class ExperienciaDeleteView(GestorRequiredMixin, DeleteView):
    model = Experiencia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:curriculo')

# --- TECNOLOGIAS ---
class TecnologiaCreateView(GestorRequiredMixin, CreateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:tecnologias')

class TecnologiaUpdateView(GestorRequiredMixin, UpdateView):
    model = Tecnologia
    form_class = TecnologiaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:tecnologias')

class TecnologiaDeleteView(GestorRequiredMixin, DeleteView):
    model = Tecnologia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:tecnologias')

# --- COMPETÊNCIAS ---
class CompetenciaCreateView(GestorRequiredMixin, CreateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:dashboard')

class CompetenciaUpdateView(GestorRequiredMixin, UpdateView):
    model = Competencia
    form_class = CompetenciaForm
    template_name = 'portfolio/crud_form.html'
    success_url = reverse_lazy('portfolio:dashboard')

class CompetenciaDeleteView(GestorRequiredMixin, DeleteView):
    model = Competencia
    template_name = 'portfolio/crud_confirm_delete.html'
    success_url = reverse_lazy('portfolio:dashboard')