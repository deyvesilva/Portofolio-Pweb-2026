from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # Agora a raiz é a Home
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('curriculo/', views.curriculo_view, name='curriculo'),
    path('tfc/', views.tfc_view, name='tfc'),
    #path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # CRUD Projetos
    path('projeto/novo/', views.ProjetoCreateView.as_view(), name='projeto_novo'),
    path('projeto/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='projeto_editar'),
    path('projeto/<int:pk>/eliminar/', views.ProjetoDeleteView.as_view(), name='projeto_eliminar'),

    # CRUD TFC
    path('tfc/novo/', views.TFCCreateView.as_view(), name='tfc_novo'),
    path('tfc/<int:pk>/editar/', views.TFCUpdateView.as_view(), name='tfc_editar'),
    path('tfc/<int:pk>/eliminar/', views.TFCDeleteView.as_view(), name='tfc_eliminar'),

    # CRUD Licenciatura & UCs
    path('licenciatura/<int:pk>/editar/', views.LicenciaturaUpdateView.as_view(), name='licenciatura_editar'),
    path('uc/nova/', views.UCCreateView.as_view(), name='uc_novo'),
    path('uc/<int:pk>/editar/', views.UCUpdateView.as_view(), name='uc_editar'),
    path('uc/<int:pk>/eliminar/', views.UCDeleteView.as_view(), name='uc_eliminar'),
    
    #CRUD competencias
    path('competencia/nova/', views.CompetenciaCreateView.as_view(), name='competencia_nova'),
    path('competencia/<int:pk>/editar/', views.CompetenciaUpdateView.as_view(), name='competencia_editar'),
    path('competencia/<int:pk>/eliminar/', views.CompetenciaDeleteView.as_view(), name='competencia_eliminar'),

    # CRUD Currículo
    path('perfil/<int:pk>/editar/', views.PerfilUpdateView.as_view(), name='perfil_editar'),
    path('experiencia/nova/', views.ExperienciaCreateView.as_view(), name='experiencia_nova'),
    path('experiencia/<int:pk>/editar/', views.ExperienciaUpdateView.as_view(), name='experiencia_editar'),
    path('experiencia/<int:pk>/eliminar/', views.ExperienciaDeleteView.as_view(), name='experiencia_eliminar'),

    # CRUD Tecnologias
    path('tecnologia/nova/', views.TecnologiaCreateView.as_view(), name='tecnologia_nova'),
    path('tecnologia/<int:pk>/editar/', views.TecnologiaUpdateView.as_view(), name='tecnologia_editar'),
    path('tecnologia/<int:pk>/eliminar/', views.TecnologiaDeleteView.as_view(), name='tecnologia_eliminar'),
]