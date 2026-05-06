from django.urls import path
from . import views

app_name = 'artigos' # Define o namespace que o teu base.html procura

urlpatterns = [
    path('', views.lista_artigos, name='lista'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe'),
    path('<int:artigo_id>/like/', views.dar_like, name='like'),
]