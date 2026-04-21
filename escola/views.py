from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Professor, Aluno
from django.shortcuts import render, get_object_or_404 # Adiciona o import

def home(request):
    return HttpResponse("Página da app escola a funcionar 🚀")


# escola/views.py

def cursos_view(request):  # Adiciona o 's' aqui
    cursos = Curso.objects.all()
    return render(request, 'escola/cursos.html', {'cursos': cursos})

def curso_view(request, id): # Esta é a de detalhe (singular)
    curso = get_object_or_404(Curso, id=id)
    return render(request, 'escola/detalhe_curso.html', {'curso': curso})

def professores_view(request):
    # Vai buscar professores e as disciplinas que cada um leciona
    professores = Professor.objects.prefetch_related('cursos').all()
    return render(request, 'escola/professores.html', {'professores': professores})

def alunos_view(request):
    # Vai buscar alunos e os cursos onde estão inscritos
    alunos = Aluno.objects.prefetch_related('cursos').all()
    return render(request, 'escola/alunos.html', {'alunos': alunos})