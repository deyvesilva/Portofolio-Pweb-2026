import json
from portfolio.models import TFC

# limpar dados antigos (opcional)
TFC.objects.all().delete()

with open('portfolio/data/tfc.json') as f:
    dados = json.load(f)

    for item in dados:
        TFC.objects.create(
            titulo=item.get('titulo', ''),
            descricao=item.get('resumo', ''),  # resumo → descricao
            ano=2025,  # não tens no JSON → valor fixo
            link=item.get('pdf', ''),  # pdf → link
            rating=item.get('rating', None),
            imagem=item.get('imagem', '')  # novo campo
        )
        
    
print("TFCs carregados com sucesso!")