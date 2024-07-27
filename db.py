from pymongo import MongoClient

def obter_db():
    # Substitua 'your_connection_string' pela sua string de conexão ao MongoDB
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['banco_de_dados_receitas']  # Nome do banco de dados
    return db

def obter_colecao_receitas():
    db = obter_db()
    return db.receitas  # Coleção de receitas
