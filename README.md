
# Python-in-FastApi-Postgres

Este é um projeto Python que utiliza a biblioteca FastApi para criar
uma API que se conecta a um banco de dados Postgres. O objetivo do
projeto é fornecer uma interface para manipulação dos dados
armazenados no banco de dados, utilizando requisições HTTP.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em seu ambiente de desenvolvimento:

- Python 3.x: https://www.python.org/downloads/
- Pip: https://pip.pypa.io/en/stable/installing/
- PostgreSQL: https://www.postgresql.org/download/

## Instalação

1. Clone este repositório para o seu ambiente local:

```shell
git clone https://github.com/seu-usuario/seu-projeto.git
```

2. Navegue até o diretório do projeto:

```shell
cd seu-projeto
```

3. Crie um ambiente virtual (opcional, mas recomendado) e ative-o:

```shell
python3 -m venv env
source env/bin/activate
```

4. Instale as dependências do projeto usando o pip:

```shell
pip install -r requirements.txt
```

## Configuração

Antes de executar o projeto, é necessário configurar a conexão com o banco de dados Postgres. Siga as etapas abaixo para realizar a configuração:

1. Abra o arquivo `config.py` localizado na raiz do projeto.
2. Edite as seguintes variáveis com as informações corretas do seu banco de dados:

```python
POSTGRES_USER = 'seu-usuario'
POSTGRES_PASSWORD = 'sua-senha'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DB = 'nome-do-banco-de-dados'
```

## Uso

Para executar o projeto, siga as etapas abaixo:

1. Certifique-se de que o ambiente virtual esteja ativado (caso tenha criado um).
2. Navegue até o diretório raiz do projeto.
3. Execute o seguinte comando:

```shell
uvicorn main:app --reload
```

4. A API estará disponível em `http://localhost:8000` por padrão.

## Endpoints

A API fornecerá os seguintes endpoints para manipulação dos dados no banco de dados:

- `GET /items`: Retorna todos os itens armazenados no banco de dados.
- `GET /items/{item_id}`: Retorna um item específico com base no ID fornecido.
- `POST /items`: Cria um novo item com base nos dados fornecidos no corpo da requisição.
- `PUT /items/{item_id}`: Atualiza um item existente com base no ID fornecido e nos dados fornecidos no corpo da requisição.
- `DELETE /items/{item_id}`: Remove um item específico com base no ID fornecido.

Certifique-se de usar um cliente HTTP (como cURL, Postman ou Insomnia) para enviar requisições para a API e testar os endpoints acima.

## Contribuição

Contribuições são bem-vindas! Se você quiser contribuir para este projeto, siga as etapas abaixo:

1. Fork este repositório.
2. Crie um novo branch com a sua contribuição: `git checkout -b minha-contribuicao`.
3. Faça as alterações desejadas e salve-as.
4. Commit suas alterações: `git commit -m '

## Demo

Insert gif or link to demo

