from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario

def lista_artigos(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})

def detalhe_artigo(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        texto = request.POST.get('comentario')
        if texto:
            Comentario.objects.create(artigo=artigo, autor=request.user, texto=texto)
            return redirect('artigos:detalhe', artigo_id=artigo.id)
            
    return render(request, 'artigos/detalhe.html', {'artigo': artigo})

@login_required
def dar_like(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:detalhe', artigo_id=artigo.id)