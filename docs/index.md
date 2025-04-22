![logo Sociall Digital](assets/img/logo.png){ .logo-center }

# Sociall Digital

## 🌟 Visão Geral

O Sociall Digital é uma aplicação web full stack desenvolvida para a Agência de Marketing e Publicidade Sociall Digital. Esta plataforma moderna e robusta oferece uma solução completa para gerenciamento de conteúdo digital e interação com clientes.

## 🚀 Funcionalidades Principais

- **Blog Integrado**: Sistema completo para publicação e gerenciamento de conteúdo
- **Portfólio de Projetos**: Showcase interativo dos trabalhos realizados
- **Sistema de Contato**: Formulário integrado para comunicação com clientes
- **Autenticação de Usuários**: Sistema seguro de login e gerenciamento de acessos
- **Interface Responsiva**: Design adaptável para todos os dispositivos

## 💻 Tecnologias Utilizadas

### Backend
- **Python 3.12+**
- **Django 5.2+**: Framework web robusto e escalável
- **PostgreSQL**: Banco de dados relacional (via psycopg2-binary)

### Frontend
- **Vite**: Build tool moderna para desenvolvimento web
- **Pillow**: Processamento de imagens

### Desenvolvimento
- **Ruff**: Linter e formatador de código Python
- **Pytest**: Framework de testes
- **Docker**: Containerização da aplicação
- **MkDocs**: Documentação com Material theme

## 🛠️ Configuração do Ambiente

### Pré-requisitos
- Python 3.12 ou superior
- Docker e Docker Compose
- Node.js (para desenvolvimento frontend)

### Comandos Principais

```bash
# Construir e iniciar os containers
task build

# Iniciar os containers
task up

# Iniciar em modo daemon
task up-d

# Parar os containers
task down

# Criar novas migrações
task makemigrations

# Executar testes
task test

# Executar verificação de código
task lint

# Formatar código
task format

# Visualizar documentação (porta 8080)
task docs
```

## 📚 Documentação

A documentação completa está disponível localmente em `http://127.0.0.1:8080` após executar o comando `task docs`. Utilize este recurso para:

- Consultar guias detalhados
- Explorar a API
- Acessar exemplos de código
- Verificar boas práticas de desenvolvimento

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Siga os padrões de código estabelecidos
4. Envie um Pull Request

## 📝 Licença

Este projeto está sob licença. Consulte o arquivo LICENSE para mais detalhes.
