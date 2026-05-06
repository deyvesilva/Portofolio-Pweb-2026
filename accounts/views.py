import secrets
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import RegistroForm
from .models import Perfil

User = get_user_model()

# --- AUTENTICAÇÃO PADRÃO (USER/PASSWORD) ---

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/register.html', {'form': form})


# --- AUTENTICAÇÃO POR LINK MÁGICO ---

def solicitar_link(request):
    """
    Passo 1 e 2: Recebe o email, gera o token e envia o link com Username + Token.
    """
    if request.method == "POST":
        email_digitado = request.POST.get('email')
        
        try:
            # 1. Procura o utilizador pelo e-mail
            user = User.objects.get(email=email_digitado)
            perfil, created = Perfil.objects.get_or_create(user=user)
            
            # 2. Gera um token único e guarda no Perfil
            token = secrets.token_urlsafe(32)
            perfil.token = token # Certifica-te que o campo no models.py se chama 'token'
            perfil.save()
            
            # 3. Monta o link com Username e Token (ajusta o domínio se necessário)
            # Exemplo: http://127.0.0.1:8000/accounts/magic-login/joao/abc123token/
            link = f"http://127.0.0.1:8000/accounts/magic-login/{user.username}/{token}/"
            
            # 4. Envia para o e-mail inserido
            send_mail(
                'Teu Link Mágico de Acesso',
                f'Olá {user.first_name}, clica no link para entrar sem senha: {link}',
                'projeto.biblioteca@gmail.com', # Teu email configurado no settings
                [email_digitado],
                fail_silently=False,
            )
            
            messages.success(request, "Verifica a tua caixa de entrada! Enviamos o link.")
            return render(request, 'accounts/email_enviado.html')
            
        except User.DoesNotExist:
            messages.error(request, "Este e-mail não está registado no nosso sistema.")
            return render(request, 'accounts/magic_link_form.html')

    return render(request, 'accounts/magic_link_form.html')


def validar_link(request, username, token):
    """
    Passo 4: Valida o token associado ao username e faz o login.
    """
    try:
        # Procura o perfil que tenha esse token E pertença ao username correto
        perfil = Perfil.objects.get(user__username=username, token=token)
        user = perfil.user
        
        # Faz o login automático
        login(request, user)
        
        # Limpa o token para segurança (não pode ser reutilizado)
        perfil.token = ""
        perfil.save()
        
        messages.success(request, f"Bem-vindo de volta, {user.first_name}!")
        return redirect('dashboard')
        
    except Perfil.DoesNotExist:
        messages.error(request, "O link é inválido, expirou ou já foi utilizado.")
        return redirect('accounts:login')
    
    # Adiciona isto ao final do teu views.py

@login_required
def dashboard_view(request):
    """
    Página protegida que o utilizador vê após o login (Magic Link ou Normal).
    """
    return render(request, 'accounts/dashboard.html', {
        'user': request.user
    })
    
    from django.contrib.auth.models import Group

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Garante que o grupo existe e adiciona o utilizador
            grupo_autores, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            login(request, user)
            return redirect('artigos:lista')
   