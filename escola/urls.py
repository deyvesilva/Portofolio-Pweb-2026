from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página de cursos
    path('cursos/', views.cursos_view, name="cursos"),
    path('curso/<int:id>', views.curso_view, name="curso_detalhe"),
    
    # Rota para a página de professores
    path('professores/', views.professores_view, name="professores"),
    
    # Rota para a página de alunos
    path('alunos/', views.alunos_view, name="alunos"),
    
    # Rota raiz da app (abre cursos por defeito)
    path('', views.cursos_view),
]