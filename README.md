
# 🎬 Cartoonflix

Uma plataforma de streaming focada em desenhos animados que marcaram a minha infância.  
Desenvolvido com Django como forma de praticar e aprimorar minhas habilidades com Python, desenvolvimento web e boas práticas de projeto.

---

## 📝 Descrição

Cartoonflix é uma aplicação web que simula uma plataforma de streaming de vídeos, com foco em cartoons nostálgicos.  
Permite listagem, visualização de detalhes, contagem de visualizações e pesquisa de filmes, além de exibir episódios relacionados.

**Destaques:**
- Construído com Django 5.1.6
- Sistema de autenticação com modelo de usuário personalizado
- Visualização de filmes e episódios
- Destaque para lançamentos e mais assistidos
- Layout dinâmico com dados injetados por context processors

---

## 📸 Demonstração

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

---

## 📚 Tabela de Conteúdos


---

## 🛠️ Instalação

### Pré-requisitos

- Python 3.10+
- pip (gerenciador de pacotes)
- Virtualenv (opcional, mas recomendado)

### Passo a passo

```bash
git clone https://github.com/seu-usuario/cartoonflix.git
cd cartoonflix
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ▶️ Como Usar

- Acesse `http://localhost:8000/` no navegador.
- Use a interface para:
  - Visualizar filmes e episódios
  - Pesquisar títulos
  - Navegar pelos mais recentes e em alta
  - Acessar detalhes e recomendações por categoria

---

## 📁 Estrutura de Pastas (resumida)

```
cartoonflix/
├── manage.py
├── cartoonflix/         
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── streaming/          
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── novos_context.py
│   └── templates/
├── static/
├── media/

```

---

## 🧰 Tecnologias Utilizadas

- Python 3.10
- Django 5.1.6
- SQLite (banco padrão)
- HTML/CSS (via templates Django)
- Bootstrap (opcional)
- Pillow (para manipulação de imagens)



---

## 👨‍💻 Autores / Agradecimentos

Desenvolvido por Breno Paiva.  
Inspirado pelos cartoons clássicos que marcaram minha infância.  
Agradecimentos especiais à comunidade Django e aos tutoriais que me ajudaram a chegar até aqui.

--