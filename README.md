
# 🚀 Portfólio Web em Django - PWEB 2026

Bem-vindo ao repositório do meu Portfólio Académico e Profissional. Esta aplicação foi desenvolvida utilizando o framework **Django**, focando-se na modularidade, dinamismo e numa experiência de utilizador completa, incluindo um sistema de blogue e autenticação moderna.

---

## 📌 Visão Geral do Projeto

O objetivo deste projeto é centralizar a gestão do meu percurso académico e profissional. A aplicação evoluiu de um portfólio estático para um ecossistema dinâmico com autenticação via **Magic Link** e uma plataforma de publicação de artigos.

### 🛠️ Funcionalidades Principais

* **Página Inicial (Dashboard):** Interface interativa com *Hero Section* e navegação fluida.
* **Gestão de Currículo & UCs:** Listagem estruturada de Perfil, Experiência, Formação e Unidades Curriculares da Licenciatura.
* **Showcase de Projetos:** Galeria com links para o GitHub e tecnologias associadas.
* **✍️ App de Artigos (Blog):** * Publicação de conteúdos sobre tecnologia e *soft-skills*.
    * Sistema de **Likes** (curtidas) aberto a todos os visitantes.
    * Sistema de **Comentários** exclusivo para utilizadores autenticados.
* **🔐 Autenticação Moderna:**
    * Login tradicional e via **Magic Link** (acesso sem senha através de token enviado por e-mail).
    * Registo de novos utilizadores com atribuição automática ao grupo de **Autores**.

---

## 🏗️ Arquitetura e Modelos

O projeto está dividido em apps modulares:
* **`portfolio`:** Core do site, gestão de projetos, tecnologias e currículo.
* **`accounts`:** Gestão de utilizadores, perfis e autenticação (Magic Links).
* **`artigos`:** Sistema de publicações, comentários e interação social.
* **`escola`:** Gestão de dados académicos e UCs.

---

## 👥 Gestão de Permissões (Grupo Autores)

Implementei um sistema de permissões baseado em grupos:
1. **Visitantes:** Podem ler artigos e dar "Likes".
2. **Utilizadores Registados:** Podem comentar em qualquer artigo.
3. **Grupo Autores:** Utilizadores com permissão para criar os seus próprios artigos e editar apenas o seu próprio conteúdo (via Dashboard/Admin).

---

## 🎨 Interface e Design

* **Layout Responsivo:** Totalmente adaptado para dispositivos móveis via CSS Grid e Flexbox.
* **Feedback Visual:** Uso de Django Messages para confirmações de login, envio de e-mails e erros.
* **UX:** Páginas de confirmação de e-mail customizadas e dashboards intuitivos.

---

## ⚙️ Acesso e Configuração

### Credenciais de Administrador:
* **Username:** `deyve`
* **Password:** `keanu123`

### Como correr o projeto localmente:
1. Clone o repositório.
2. Instale as dependências: `pip install django`
3. Aplique as migrações: `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`
5. **Nota sobre E-mails:** Os Magic Links são impressos no **terminal** (console backend) para fins de desenvolvimento.

---

## 🔒 Painéis de Gestão

O projeto dispõe de dois níveis de controlo:
* **Dashboard Customizado:** `http://localhost:8000/accounts/dashboard/` (Gestão rápida de perfil).
* **Painel Administrativo:** `http://localhost:8000/admin/` (Controlo total de modelos e utilizadores).
