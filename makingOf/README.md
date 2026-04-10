# Making Of – Projeto Portfolio Django

## 1. Introdução

Este documento descreve o processo de desenvolvimento do projeto Portfolio desenvolvido em Django. Inclui decisões de modelação, problemas encontrados, soluções aplicadas e utilização de ferramentas de apoio.

---

## 2. Decisões de Modelação

### Tecnologia

1. Foi utilizado um campo ImageField para armazenar o logo, permitindo associar visualmente cada tecnologia e melhorar a apresentação no admin e no frontend.
2. O campo nivel foi definido com choices (1 a 5) para normalizar os dados e garantir consistência na avaliação das tecnologias.

### Projeto

1. Foi utilizada uma relação ManyToMany com Tecnologia para permitir que um projeto utilize várias tecnologias, refletindo a realidade de desenvolvimento de software.
2. A utilização de ForeignKey para UnidadeCurricular permite associar cada projeto a uma unidade curricular específica, mantendo integridade referencial.

### TFC

1. O campo rating foi limitado entre 1 e 5 usando validadores, garantindo que os valores inseridos são válidos e consistentes.
2. A relação ManyToMany com Tecnologia permite identificar facilmente as tecnologias utilizadas em cada trabalho final de curso.

### Experiência

1. Foi utilizada uma ForeignKey para Perfil para associar cada experiência a um utilizador específico, garantindo organização dos dados.
2. A relação ManyToMany com Competencia e Tecnologia permite representar múltiplas competências e ferramentas utilizadas numa experiência profissional.

### Formação

1. O uso de DateField permite armazenar datas de forma estruturada, facilitando ordenação e filtragem.
2. A relação ManyToMany com Competencia permite associar várias competências adquiridas em cada formação.

### Unidade Curricular

1. Foi utilizada uma ForeignKey para Licenciatura para manter a ligação entre unidades curriculares e o curso correspondente.
2. O campo imagem foi incluído para enriquecer visualmente a apresentação das unidades curriculares.

### Licenciatura

1. A entidade foi separada para evitar redundância de dados ao associar várias unidades curriculares ao mesmo curso.
2. Os campos nome e universidade permitem identificar claramente o contexto académico.

### Perfil

1. A entidade Perfil foi criada para centralizar informação do utilizador, permitindo reutilização noutras entidades como Experiência e Formação.
2. O campo bio é opcional (null=True, blank=True), permitindo flexibilidade no preenchimento dos dados.

### Competência

1. Foi criada como entidade independente para evitar repetição de dados e permitir reutilização em múltiplos contextos.
2. A sua utilização em relações ManyToMany permite associar várias competências a diferentes entidades.

---

## 3. Problemas Encontrados e Soluções

### Problema 1: Erro "no such column"

* Causa: Alterações nos modelos sem aplicar migrações.
* Solução: Execução dos comandos:

  * python manage.py makemigrations
  * python manage.py migrate

### Problema 2: Imagens não apareciam

* Causa: Configuração incompleta de MEDIA_URL e MEDIA_ROOT.
* Solução:

  * Configuração no settings.py
  * Adição de static() no urls.py
  * Criação da pasta media/

### Problema 3: Estrutura incorreta da pasta media

* Causa: Mistura de código Django com ficheiros de media.
* Solução:

  * Separação clara entre apps e media
  * Uso de media apenas para imagens e ficheiros

### Problema 4: Conflitos no Git

* Causa: Alterações estruturais (movimento de pastas).
* Solução:

  * Uso de git pull --rebase
  * Correção manual da estrutura
  * Organização adequada do repositório

---

## 4. Importação de Dados (JSON)

Foi implementado um sistema de importação automática de dados de TFC através de um ficheiro JSON.

### Passos:

1. Criação da pasta `portfolio/data`
2. Adição do ficheiro `tfc.json`
3. Criação do script `loader.py`

### Funcionamento:

* O script lê o ficheiro JSON
* Percorre os dados
* Cria automaticamente objetos TFC na base de dados usando o ORM do Django

### Execução:

* python manage.py shell
* from portfolio import loader

---

## 5. Organização de Ficheiros de Media

Foi criada a pasta `media/` para armazenar:

* logos de tecnologias
* imagens de projetos
* imagens de unidades curriculares

Estrutura:

* media/tecnologias/
* media/projetos/
* media/ucs/

---

## 6. Uso de Ferramentas de IA

Foram utilizadas ferramentas de Inteligência Artificial como apoio ao desenvolvimento, nomeadamente para:

* resolução de erros Django
* configuração do admin
* criação do script de importação JSON
* organização da estrutura do projeto

A utilização de IA permitiu acelerar o processo de desenvolvimento e melhorar a qualidade das soluções implementadas, embora todas as decisões tenham sido compreendidas e adaptadas ao contexto do projeto.

---

## 7. Melhorias Futuras

* Desenvolvimento de interface frontend para visualização dos dados
* Implementação de sistema de pesquisa e filtros
* Associação automática de tecnologias a partir do texto dos TFC
* Melhorias na interface do admin

---

## 8. Conclusão

A modelação foi pensada para garantir organização, reutilização e escalabilidade dos dados. O uso de Django ORM permitiu uma gestão eficiente da base de dados e a integração de dados externos (JSON) tornou o sistema mais dinâmico.

O projeto cumpre os objetivos propostos, apresentando uma estrutura consistente, funcional e extensível.
