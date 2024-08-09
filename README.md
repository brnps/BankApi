# Projeto FastAPI

Este é um projeto FastAPI que implementa uma API para gerenciamento de contas com funcionalidades de depósito, saque, transferência e consulta de saldo.

## Requisitos

- Python 3.8 ou superior
- [pip](https://pip.pypa.io/en/stable/)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/brnps/BankApi.git
   cd seu-repositorio
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   ```
3. **Ative o ambiente virtual:**

   No Windows:
   ```bash
   venv\Scripts\activate
   ```
   No macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
3. **Instale as dependências:**

  ```bash
   source venv/bin/activate
   ```

3. **Executando o Projeto:**

  1.Inicie o servidor FastAPI:
  
  ```bash
   uvicorn app.main:app --reload
   ```
  Onde "app.main:app" é o caminho para o objeto FastAPI no seu projeto.
  
  2.Acesse a API:

  Abra seu navegador e vá para http://127.0.0.1:8000. Você pode usar o Swagger UI para explorar e testar a API.

   
