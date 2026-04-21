from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def home(request):
    return HttpResponse("Página da app escola a funcionar 🚀")


def cursos_view(request):

    cursos = (Curso.objects
               .select_related('professor')
               .prefetch_related('alunos')
               .all()
    )
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})