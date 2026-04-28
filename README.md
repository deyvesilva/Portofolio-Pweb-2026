# 🚀 Portfólio Web em Django - PWEB 2026

Bem-vindo ao repositório do meu Portfólio Académico e Profissional. Esta aplicação foi desenvolvida utilizando o framework **Django**, focando-se na modularidade, dinamismo e uma interface de utilizador intuitiva e responsiva.

---

## 📌 Visão Geral do Projeto

O objetivo deste projeto foi criar uma plataforma centralizada para a gestão do meu percurso. A aplicação não é apenas um site estático, mas um sistema dinâmico onde toda a informação é gerida através de uma base de dados relacional.

### 🛠️ Funcionalidades Principais

* **Página Inicial (Dashboard):** Interface baseada em cartões interativos com uma *Hero Section* moderna e efeitos de navegação fluida.
* **Gestão de Currículo:** Agregação de Perfil, Experiência Profissional, Formação Académica e Competências.
* **Licenciatura & UCs:** Listagem estruturada de Unidades Curriculares, organizada por anos e semestres.
* **Showcase de Projetos:** Galeria de projetos com integração de links externos (GitHub) e tecnologias utilizadas.
* **Destaque TFC:** Secção dedicada ao Trabalho de Fim de Curso com sistema de avaliação (rating).
* **Integração de Dados:** Consumo de ficheiros JSON e APIs externas para enriquecer o sistema.

---

## 🏗️ Estrutura de Modelos (Base de Dados)

A aplicação utiliza um modelo de dados robusto:
* **Área de Currículo:** `Perfil`, `Experiencia`, `Formacao`, `Competencia`.
* **Área Académica:** `Licenciatura`, `UnidadeCurricular`.
* **Área de Portfólio:** `Projeto`, `Tecnologia`, `TFC`.
* **Documentação:** `MakingOf`.

---

## 🎨 Interface e Design

* **Layout Responsivo:** Adaptado para todos os dispositivos via CSS Grid e Flexbox.
* **Tipografia:** Implementação de `text-align: justify` para uma leitura profissional.
* **UX:** Imagens de fundo temáticas e efeitos de *hover* nos cartões de navegação.

---

## 🔐 Acesso à Administração

* **Username:** `deyve`
* **Password:** `admin1234`


## 🛠️ Painel de Gestão (Dashboard)

Além da administração nativa do Django, o projeto inclui um **Dashboard de Gestão Customizado**. Este painel permite realizar operações de CRUD (Criar, Ler, Atualizar e Eliminar) de forma centralizada em todos os modelos do portfólio, sem a necessidade de navegar por menus complexos.

### Como Aceder:
1. Certifique-se de que o servidor está a correr: `python manage.py runserver`
2. Aceda ao URL direto: http://localhost:8000/dashboard/
3. Através deste painel, pode gerir:
   * **Perfil & Licenciatura:** Edição rápida de bios e descrições.
   * **Conteúdo:** Adicionar ou remover Projetos, UCs, Competências e Experiências.
   * **Visualização:** As alterações feitas aqui refletem-se instantaneamente nas páginas públicas de visualização.

---

## 🔒 Gestão de Conteúdo (Privado)

Para garantir uma experiência de visualização limpa e profissional, todas as funcionalidades de gestão (**Criar, Editar e Eliminar**) foram removidas das páginas públicas do portfólio. 

A gestão do site é agora feita centralizadamente através de um **Dashboard de Administração**:
* **URL de Gestão:** `http://localhost:8000/dashboard/`
* **Objetivo:** Centralizar o controlo de Perfil, Licenciatura, Projetos e Competências num único local seguro, mantendo o front-end do portfólio focado apenas na apresentação de conteúdos.
