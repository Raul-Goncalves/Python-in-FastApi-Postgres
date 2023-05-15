import asyncpg

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    produto_id: int
    nome: str
    preco: float
    quantidade: int


class DBManager:
    def __init__(self, app):
        self._app = app

    async def connect(self):
        self._app.state.pool = await asyncpg.create_pool(
            host="localhost",
            database="Loja",
            user="postgres",
            password="123",
        )

    async def disconnect(self):
        await self._app.state.pool.close()

    async def fetch(self, query, *args):
        async with self._app.state.pool.acquire() as conn:
            return await conn.fetch(query, *args)

    async def execute(self, query, *args):
        async with self._app.state.pool.acquire() as conn:
            return await conn.execute(query, *args)


db = DBManager(app)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
def Loja_de_Produtos():
    return 'Digite "http://127.0.0.1:8000/docs#/" para visualizar o menus da nossa loja'


@app.get("/produtos")
async def produtos_todos():
    query = "SELECT * FROM produtos"
    rows = await db.fetch(query)
    return {"resultados": rows}


@app.post("/produtos")
async def criar_produto(item: Item):
    query = "INSERT INTO produtos (id, nome, preco, quantidade) VALUES ($1, $2, $3, $4)"
    await db.execute(query, item.produto_id, item.nome, item.preco, item.quantidade)
    return "Produto criado com sucesso!"


@app.get("/produtos/{id}")
async def ler_produto(id: int):
    query = "SELECT * FROM produtos WHERE id = $1"
    product = await db.fetch(query, id)
    return product


@app.delete("/produtos/{id}")
async def deletar_produto(id: int):
    query = "DELETE FROM produtos WHERE id = $1"
    await db.execute(query, id)
    return f"Produto com id={id} foi deletado com sucesso."


@app.put("/produtos/{id}")
async def update_produto(id: int, item: Item):
    query = "UPDATE produtos SET nome=$1, preco=$2, quantidade=$3 WHERE id=$4"
    await db.execute(query, item.nome, item.preco, item.quantidade, id)
    return f"Produto com ID={id} foi atualizado com sucesso"
