# 📘 Making Of – Projeto Portfolio Django

## 📌 1. Introdução

Este projeto consistiu no desenvolvimento de uma aplicação web em Django para gestão de um portfólio académico e profissional. O sistema permite armazenar e visualizar informação relativa a projetos, tecnologias, competências, formação, experiência profissional e trabalhos finais de curso (TFC).

Foram também integradas fontes externas de dados, nomeadamente ficheiros JSON e APIs da Universidade Lusófona.

---

## 🧱 2. Modelação do Sistema

### 🔹 Decisões gerais

* Utilização do **Django ORM** para garantir consistência e facilidade na manipulação de dados.
* Separação do sistema em **várias entidades (models)** para garantir normalização.
* Uso de relações **ForeignKey** e **ManyToMany** para refletir relações reais.

---

## 🧠 3. Justificação das Decisões de Modelação

### 👤 Perfil

* Separado das restantes entidades para permitir reutilização (ex: experiência, formação).
* Permite centralizar informação pessoal.

---

### 🎓 Licenciatura

* Criada como entidade própria para permitir ligação com várias unidades curriculares.
* Facilita futura expansão (ex: vários cursos).

---

### 📚 Unidade Curricular

* Relacionada com Licenciatura (ForeignKey).
* Permite estruturar o curso de forma organizada.
* Inclui imagem para representação visual.

---

### 💻 Tecnologia

* Criada como entidade independente para reutilização em múltiplos contextos.
* Relação ManyToMany com Projetos, TFC e Experiência.
* Inclui:

  * nível (1–5)
  * logo (ImageField)

---

### 🧠 Competência

* Separada de Tecnologia para distinguir conhecimentos técnicos de competências gerais.
* Permite associação a múltiplas entidades.

---

### 📁 Projeto

* Relacionado com:

  * Unidade Curricular
  * Tecnologias
  * Competências
* Permite representar projetos académicos com contexto completo.

---

### 💼 Experiência

* Relacionada com Perfil.
* Permite associar tecnologias e competências usadas no contexto profissional.

---

### 🎓 Formação

* Semelhante à experiência, mas focada em formação complementar.
* Permite associar competências adquiridas.

---

### 🧪 TFC (Trabalho Final de Curso)

* Criado como entidade independente.
* Inclui:

  * título
  * descrição
  * rating
  * imagem (vinda do JSON)
* Relacionado com tecnologias.

---

### 🛠️ Making Of

* Criado como entidade para documentar o processo de desenvolvimento.
* Inclui:

  * decisões
  * erros
  * justificações
  * uso de IA

---

## 🖼️ 4. Gestão de Imagens

* Utilização de `ImageField` para armazenar imagens.
* Configuração de:

  * `MEDIA_ROOT`
  * `MEDIA_URL`
* Organização dos ficheiros em:

  ```
  media/
    ├── tecnologias/
    ├── projetos/
    ├── ucs/
    └── makingof/
  ```

### Problema encontrado:

* Imagens não apareciam no admin.

### Solução:

* Configuração correta do `urls.py`:

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 📊 5. Importação de Dados (JSON)

### ✔ TFCs

Foi desenvolvido um script (`loader.py`) para importar dados de um ficheiro JSON.

### Processo:

* Leitura do ficheiro JSON
* Criação de objetos TFC via ORM

### Problemas encontrados:

* Campos com nomes diferentes (ex: `courseName` vs `name`)
* Dados inconsistentes

### Soluções:

* Uso de `.get()` para evitar erros
* Ajuste manual dos campos

---

## 🌐 6. Integração com API Lusófona

Foram utilizados endpoints da API para obter:

* Informação do curso
* Unidades curriculares

### Problemas encontrados:

#### ❌ Erro:

```
KeyError: 'name'
```

✔ Solução:

* Uso correto de:

```python
data['courseDetail']['courseName']
```

---

#### ❌ Erro:

```
ValueError: invalid literal for int() with base 10: '1º Semestre'
```

✔ Solução:

* Conversão de string para inteiro

---

#### ❌ Erro:

```
ValueError: 'Anual'
```

✔ Solução:

```python
if "1" in semestre_str:
    semestre = 1
elif "2" in semestre_str:
    semestre = 2
else:
    semestre = 0
```

---

## ⚙️ 7. Administração (Admin Django)

Foi configurado o admin para:

* Visualização de imagens (logos e thumbnails)
* Filtros
* Pesquisa
* Relações ManyToMany com interface melhorada

---

## 🧪 8. Problemas e Erros Encontrados

* Erros de migração (`no such column`)
* Apps não registadas no `INSTALLED_APPS`
* Problemas com imagens (media)
* Conflitos no Git (merge/rebase)
* Estrutura errada (apps dentro de media)

---

## 🤖 9. Uso de Inteligência Artificial

A IA foi utilizada como apoio no desenvolvimento:

* Resolução de erros técnicos
* Explicação de conceitos Django
* Criação e melhoria de código
* Estruturação do projeto
* Apoio na escrita do Making Of

---

## 📦 10. Versionamento (Git)

* Uso de commits frequentes
* Mensagens descritivas
* Resolução de conflitos com `rebase`

---

## ✅ 11. Conclusão

O projeto permitiu consolidar conhecimentos em:

* Django
* Modelação de dados
* APIs
* JSON
* Upload de ficheiros
* Git

Foram enfrentados vários desafios técnicos, resolvidos com sucesso, resultando numa aplicação funcional, estruturada e extensível.

---
