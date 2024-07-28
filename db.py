from pymongo import MongoClient
import os

def obter_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")
    cliente = MongoClient(mongo_uri)
    db = cliente['banco_de_dados_receitas']  # Nome do banco de dados
    return db

def obter_colecao_receitas():
    db = obter_db()
    return db.receitas  # Coleção de receitas
