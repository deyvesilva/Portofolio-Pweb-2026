from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'), # Agora a raiz é a Home
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('curriculo/', views.curriculo_view, name='curriculo'),
    path('tfc/', views.tfc_view, name='tfc'),
]