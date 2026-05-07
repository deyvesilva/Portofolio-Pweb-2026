# 📘 Making Of – Projeto Portfolio Django (Versão Consolidada 2026)

## 📌 1. Introdução
Este projeto consistiu no desenvolvimento de uma aplicação web em Django para gestão de um portfólio académico e profissional. O sistema evoluiu de um repositório de dados estático para uma plataforma dinâmica que permite gerir projetos, tecnologias, competências e uma nova área de blogue (Artigos), integrando um sistema de autenticação moderno via **Magic Link** e uma área de utilizadores (`accounts`).

---

## 🧱 2. Modelação do Sistema

### 🔹 Decisões Gerais
* Utilização do **Django ORM** para garantir consistência e facilidade na manipulação de dados.
* Separação do sistema em **apps modulares** (`portfolio`, `escola`, `accounts`, `artigos`).
* Uso de relações **ForeignKey** e **ManyToMany** para refletir a complexidade das relações entre UCs, Projetos e Tecnologias.

---

## 🧠 3. Justificação das Decisões de Modelação

### 👤 App Accounts & Perfil
* **Centralização:** A app `accounts` gere a identidade do utilizador. O modelo Perfil permite centralizar informação pessoal que é reutilizada em experiências e formações.
* **🔐 Magic Link:** Implementado em `accounts` para permitir login sem password via token, aumentando a segurança e usabilidade.

### 🎓 Licenciatura & Unidade Curricular
* Entidades próprias que refletem a estrutura académica da Universidade Lusófona.
* Relacionadas via **ForeignKey**, permitindo organizar o curso por anos e semestres.

### 💻 Tecnologia & Competência
* Entidades independentes para evitar duplicação. Uma tecnologia (ex: Python) pode estar associada a vários Projetos, TFCs ou Experiências Profissionais.

### 📁 Projeto & TFC
* O **Projeto** agrega UCs, Tecnologias e Competências.
* O **TFC** (Trabalho Final de Curso) funciona como uma entidade independente com sistema de rating e integração de dados via JSON.

### ✍️ App Artigos
* Criada para publicação de conteúdos técnicos e *soft-skills*.
* **Comentários:** Relacionados com o utilizador (`User`) e o `Artigo`.
* **Likes:** Implementados como `ManyToManyField` para permitir interatividade social aberta a todos.

---

## 🏗️ 4. Arquitetura MVT (Model-View-Template)

O projeto segue rigorosamente a separação de responsabilidades do Django:

* **Model:** Define a estrutura da base de dados e regras de negócio.
* **View:** Atua como intermediário, processando a lógica (ex: verificar se o token do Magic Link é válido ou filtrar os artigos do próprio autor) e recolhendo dados.
* **Template:** Gere a apresentação final (HTML/CSS), utilizando herança de templates para manter a consistência visual.



---

## 👥 5. Gestão de Permissões e Grupos

* **Grupo "Autores":** Criado via Admin e associado automaticamente a novos utilizadores no registo (via `accounts`).
* **Controlo Granular:** No `admin.py` da app `artigos`, foi sobrescrito o método `get_queryset` para que utilizadores do grupo Autores apenas consigam editar os seus próprios artigos, enquanto Superusers mantêm controlo total.

---

## 🖼️ 6. Gestão de Imagens e Media

* Configuração de `MEDIA_ROOT` e `MEDIA_URL`.
* **Solução para exibição:** Integração de `static(settings.MEDIA_URL, ...)` no `urls.py` principal para permitir a visualização de logos e fotografias de projetos no browser.

---

## 📊 7. Importação de Dados (JSON & API)

### ✔ TFCs via JSON
* Uso de um script `loader.py` para ler dados externos.
* Tratamento de inconsistências nos campos do JSON (ex: mapeamento de nomes de cursos).

### 🌐 API Lusófona
* Consumo de endpoints para obter detalhes de Unidades Curriculares.
* **Desafio Técnico:** Tratamento de erros de tipo (`KeyError`) e conversão de strings de semestre ("1º Semestre") para inteiros para filtragem na base de dados.

---

## 🧪 8. Problemas e Erros Encontrados

* **Migrações:** Erros de `no such column` resolvidos com limpeza de migrações e `makemigrations`.
* **Namespaces:** Erro `NoReverseMatch` corrigido ao definir corretamente `app_name` nos ficheiros `urls.py` de cada app.
* **Templates:** Erros de `TemplateDoesNotExist` resolvidos através da organização correta das pastas `templates/app_name/`.
* **Permissões:** Conflitos onde autores viam posts alheios, resolvidos com lógica personalizada no `ModelAdmin`.

---

## 🤖 9. Uso de Inteligência Artificial

A IA foi utilizada de forma estratégica para:
* Depuração de erros complexos de lógica (Magic Link tokens).
* Aceleração da escrita de código repetitivo (*boilerplate*).
* Estruturação documental e explicação de conceitos da arquitetura Django.

---

## 📦 10. Versionamento (Git)

* Utilização de Git para controlo de versões.
* Gestão de conflitos durante o desenvolvimento de múltiplas funcionalidades (Auth e Artigos).

---

## ✅ 11. Conclusão
O desenvolvimento deste portfólio demonstrou a robustez do Django para criar sistemas modulares. A integração da app `accounts` com o sistema de `artigos` e a base de dados académica resultou numa aplicação completa, segura e funcional, pronta para expansão futura.