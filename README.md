# Flask Authentication API 🛡️

Este projeto é uma API RESTful desenvolvida em Python com o framework Flask, focada em autenticação de usuários e controle de permissões (RBAC). Faz parte do desafio de desenvolvimento backend da trilha Python da Rocketseat.

## Funcionalidades

- **CRUD de Usuários:** Criação, leitura, atualização e exclusão de usuários.
- **Autenticação:** Sistema de login e logout utilizando `Flask-Login`.
- **Segurança:** Hashing de senhas com `bcrypt` para garantir que dados sensíveis não sejam salvos em texto plano.
- **Controle de Acesso:** - Usuários comuns podem visualizar perfis e editar a própria senha.
  - Apenas administradores (`role='admin'`) podem deletar usuários.
- **Persistência:** Integração com banco de dados MySQL via SQLAlchemy.

## Tecnologias Utilizadas

* **Python 3**
* **Flask** (Micro-framework web)
* **SQLAlchemy** (ORM)
* **Flask-Login** (Gerenciamento de sessão)
* **Bcrypt** (Criptografia)
* **PyMySQL** (Driver MySQL)

## Pré-requisitos

Antes de começar, você precisará ter instalado:
- Python 3.x
- MySQL Server

##  Configuração

### 1. **Clone o repositório:**
   ```bash
   git clone https://github.com/edelsonerickson95/sample-flask-auth.git
   ```
### 2 Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3 Instale as dependências:

```Bash
pip install -r requirements.txt
```

### Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto e preencha com suas credenciais:

Snippet de código
SECRET_KEY="sua_chave_secreta"
MYSQL_USER="seu_usuario"
MYSQL_PASSWORD="sua_senha"
MYSQL_DATABASE="nome_do_banco"
MYSQL_HOST="localhost"

### Como executar
Para iniciar o servidor de desenvolvimento:

```Bash
python app.py
A API estará disponível em http://127.0.0.1:5000.
``