# API de Busca de Operadoras de Saúde

API RESTful para busca e consulta de informações sobre operadoras de planos de saúde registradas na ANS (Agência Nacional de Saúde Suplementar).

## Tecnologias Utilizadas

- **Python 3.13**: Linguagem de programação utilizada
- **FastAPI**: Framework web de alta performance para construção de APIs
- **SQLAlchemy**: ORM para acesso ao banco de dados
- **PostgreSQL**: Sistema de gerenciamento de banco de dados
- **Pydantic**: Biblioteca para validação de dados e configurações

## Estrutura do Projeto

```
.
├── database/
│   └── database.py             # Configurações de conexão com o banco de dados
├── exceptions/
│   └── database_exceptions.py  # Exceções personalizadas
├── models/
│   ├── operadora_dto.py        # DTO para transferência de dados
│   ├── operadora_model.py      # Modelo de dados do SQLAlchemy
│   ├── operadora_pagination.py # Modelo para paginação de resultados
│   └── operadora_schema.py     # Schema para validação de dados
├── routers/
│   └── operadora_router.py     # Rotas da API
├── services/
│   └── operadora_service.py    # Lógica de negócios
├── LICENSE.md                  # Arquivo de licença
├── main.py                     # Ponto de entrada da aplicação
└── README.md                   # Arquivo de instrução
```

## Configuração e Instalação

### Requisitos

- Python 3.13+
- PostgreSQL 

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/brunomourasoares/4a--testeapi-python.git
cd 4a--testeapi-python
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados:
   - Crie um banco de dados PostgreSQL chamado `ans_database`
   - O usuário padrão é `python` com senha `python123456` (altere conforme necessário no arquivo database.py)

4. Execute o VENV
```bash
.\venv\Scripts\activate
```

5. Execute a aplicação
```bash
uvicorn main:app --reload
```

## Endpoints

### Endpoint de Saúde

```
GET /health
```

Verifica o status da API e a conexão com o banco de dados.

**Resposta de Sucesso:**
```json
{
  "status": "ok",
  "database": "connected"
}
```

### Endpoint de Busca de Operadoras

```
GET /api/operadoras/
```

Busca operadoras de saúde com base em um termo de pesquisa.

**Parâmetros de Consulta:**
- `termo` (obrigatório): Termo para busca (CNPJ, Razão Social, Nome Fantasia, etc.)
- `pagina` (opcional, padrão=1): Página atual dos resultados
- `quantidade` (opcional, padrão=10): Quantidade de itens por página (máx. 100)

**Resposta de Sucesso:**
```json
{
  "items": [
    {
      "registro_ans": 123456,
      "cnpj": "12345678901234",
      "razao_social": "OPERADORA EXEMPLO S.A.",
      "modalidade": "MEDICINA DE GRUPO",
      "logradouro": "RUA EXEMPLO",
      "numero": "123",
      "complemento": "SALA 1",
      "bairro": "CENTRO",
      "cidade": "SÃO PAULO",
      "uf": "SP",
      "ddd": "11",
      "telefone": "12345678",
      "endereco_eletronico": "contato@exemplo.com",
      "representante": "NOME DO REPRESENTANTE"
    }
  ],
  "total": 50,
  "pagina": 1,
  "quantidade": 10,
  "paginas": 5,
  "tem_proximo": true,
  "tem_anterior": false
}
```

## Tratamento de Erros

### Erro de Conexão com Banco de Dados

**Resposta (503 Service Unavailable):**
```json
{
  "detail": "O serviço está temporariamente indisponível. O banco de dados está offline."
}
```

## Modelo de Dados

### Operadora

Representa uma operadora de plano de saúde registrada na ANS.

**Campos principais:**
- `registro_ans`: Número de registro na ANS (chave primária)
- `cnpj`: CNPJ da operadora
- `razao_social`: Nome oficial da empresa
- `nome_fantasia`: Nome comercial
- `modalidade`: Tipo de operadora (ex: Medicina de Grupo, Seguradora)
- `uf`: Estado da sede
- `cidade`: Cidade da sede
- `representante`: Nome do representante legal

## Licença
[MIT License](./License.md)

## Autor
Desenvolvido por [Bruno Moura Soares](https://www.linkedin.com/in/brunomsoares/)