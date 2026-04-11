import json
from portfolio.models import TFC
from portfolio.models import Licenciatura, UnidadeCurricular

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

# apagar dados antigos (opcional)
UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()

with open('portfolio/data/api/curso_PT.json', encoding='utf-8') as f:
    data = json.load(f)

# criar licenciatura
lic = Licenciatura.objects.create(
    nome=data['courseDetail']['courseName'],
    universidade="Universidade Lusófona",
    descricao="Curso importado automaticamente da API"
)

# criar UCs
for uc in data['courseFlatPlan']:

    semestre_str = uc.get('semester', '')

    if "1" in semestre_str:
        semestre = 1
    elif "2" in semestre_str:
        semestre = 2
    else:
        semestre = 0

    UnidadeCurricular.objects.create(
        nome=uc['curricularUnitName'],
        ano=uc['curricularYear'],
        semestre=semestre,
        descricao="Importado da API",
        licenciatura=lic
    )

print("Curso e UCs carregados na BD!")