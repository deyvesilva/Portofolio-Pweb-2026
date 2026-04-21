from django.shortcuts import render
from .models import * # Importa todos os teus modelos

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
    # Usamos prefetch_related para otimizar a consulta das ManyToMany
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