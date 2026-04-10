# Making Of – Projeto Portfolio Django

## 1. Decisões tomadas

* Utilização de Django ORM para modelação dos dados
* Separação das entidades (TFC, Projeto, Tecnologia, etc)
* Uso de ImageField para gestão de imagens

## 2. Modelação

* Relações ManyToMany entre projetos, tecnologias e competências
* Uso de ForeignKey para relações principais
* Normalização dos dados para evitar redundância

## 3. Problemas encontrados

* Erro "no such column" → resolvido com migrations
* Imagens não apareciam → resolvido com MEDIA_URL e MEDIA_ROOT
* Conflitos no Git → corrigido ao separar media de apps

## 4. Importação de dados (JSON)

* Criação de script loader.py
* Leitura de ficheiro JSON com dados de TFC
* Inserção automática na base de dados

## 5. Uso de IA

* Utilizada para:

  * resolução de erros Django
  * criação de admin.py
  * estruturação do loader JSON
* A IA ajudou a acelerar o desenvolvimento e debugging

## 6. Melhorias futuras

* Interface frontend para mostrar dados
* Filtros e pesquisa
* Ligação automática de tecnologias via texto
