# Sociall Digital Core

## 📝 Descrição
Aplicação web full stack desenvolvida para a Agência de Marketing e Publicidade Sociall Digital. O projeto oferece funcionalidades essenciais para a visibilidade da Agência, como blog, portfólio de projetos, formulário de contato e sistema de login.

## 🛠️ Tecnologias Principais

### Backend
- Python 3.12+
- Django 5.2
- PostgreSQL (via psycopg2-binary)
- Django Vite

### Frontend
- Vite.js
- TailwindCSS
- DaisyUI
- Alpine.js
- HTMX

## 🚀 Características
- Blog integrado
- Portfólio de projetos
- Sistema de contato
- Autenticação de usuários
- Interface responsiva
- Documentação com MkDocs

## 📦 Pré-requisitos
- Python 3.12 ou superior
- UV (gerenciador de pacotes Python)
- Node.js e npm
- Docker e Docker Compose

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/matheusfabiao/sociall-digital-core.git
cd sociall-digital-core
```

2. Instale as dependências Python com UV:
```bash
uv pip install -e .
```

3. Instale as dependências de desenvolvimento (opcional):
```bash
uv pip install -e ".[dev,doc]"
```

4. Instale as dependências JavaScript:
```bash
npm install
```

## 🚀 Executando o Projeto

### Desenvolvimento com Docker

1. Caso seja a primeira vez, construa os containers:
```bash
task build
```

2. Inicie o container normalmente ou em modo daemon:
```bash
task up
task up-d
```

### Desenvolvimento Local

1. Execute o servidor Django:
```bash
python src/manage.py runserver
```

2. Em outro terminal, inicie o Vite:
```bash
npm run dev
```

## 📚 Documentação
Para visualizar a documentação localmente:
```bash
task docs
```
A documentação estará disponível em `http://127.0.0.1:8080`

## 🧪 Testes
Execute os testes com:
```bash
task test
```

## 🔍 Linting e Formatação
- Verificar código:
```bash
task lint
```

- Formatar código:
```bash
task format
```

## 🤝 Contribuindo
1. Faça o fork do projeto
2. Crie sua branch de feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Este projeto está sob a licença ISC. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores
- Matheus Fabião

## 🙏 Agradecimentos
- Equipe Sociall Digital
- Dev Matheus Fabião
- Comunidade Django
- Contribuidores do projeto