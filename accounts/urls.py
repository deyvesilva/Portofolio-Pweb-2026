from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # --- Autenticação Tradicional ---
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # --- Autenticação por Link Mágico ---
    # O 'name' tem de ser exatamente 'solicitar_link' para o teu template funcionar
    path('solicitar-link/', views.solicitar_link, name='solicitar_link'),
    
    path('validar/<str:username>/<str:token>/', views.validar_link, name='validar_magic_link'),

    # --- Páginas de Destino ---
    path('dashboard/', views.dashboard_view, name='dashboard'),
]