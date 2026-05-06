from django.contrib.auth import get_user_model, login
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) # Inicia a sessão
            # Redireciona para o dashboard após o login (ou 'home' se preferires)
            return redirect('dashboard') 
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request) # Termina a sessão
    return redirect('accounts:login')

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redireciona para a home após o registo bem-sucedido
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/register.html', {'form': form})

User = get_user_model()

def magic_link_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Gerar token e UID
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Criar o link (ajusta o domínio se necessário)
            link = f"{request.build_absolute_uri('/accounts/magic-login/')}{uid}/{token}/"
            
            # Enviar e-mail (Configura o EMAIL_BACKEND no settings.py para ver no terminal)
            send_mail(
                'O teu Link Mágico',
                f'Clica aqui para entrar: {link}',
                'noreply@portfolio.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, "Verifica o teu e-mail para o link de acesso!")
        except User.DoesNotExist:
            messages.error(request, "E-mail não encontrado.")
            
    return render(request, 'accounts/magic_link_form.html')

def magic_login(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect('dashboard')
    else:
        messages.error(request, "O link é inválido ou expirou.")
        return redirect('accounts:login')