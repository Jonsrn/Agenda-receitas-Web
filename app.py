from flask import Flask, render_template, request, redirect, url_for
from db import obter_colecao_receitas
from bson import ObjectId

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inserir_receitas', methods=['GET', 'POST'])
def inserir_receitas():
    if request.method == 'POST':
        receitas = obter_colecao_receitas()
        dados_receita = {
            'tipo': request.form.get('tipo'),
            'categoria': request.form.get('categoria'),
            'tipo_prato': request.form.get('tipo_prato'),
            'pais_origem': request.form.get('pais_origem'),
            'nome_receita': request.form.get('nome_receita'),
            'tempo_preparo': request.form.get('tempo_preparo'),
            'ingredientes': request.form.getlist('ingrediente_nome[]'),
            'quantidades': request.form.getlist('ingrediente_quantidade[]'),
            'unidades': request.form.getlist('ingrediente_unidade[]'),
            'modo_preparo': request.form.get('modo_preparo'),
        }
        receitas.insert_one(dados_receita)  # Inserindo a receita no MongoDB
        return redirect(url_for('home'))
    return render_template('inserir_receitas.html')

@app.route('/consultar', methods=['GET'])
def consultar_receitas():
    consulta = request.args.get('search', '')
    categoria = request.args.get('categoria', '')
    receitas_encontradas = []
    if consulta:
        receitas = obter_colecao_receitas()
        filtro = {"$and": [{"nome_receita": {"$regex": consulta, "$options": "i"}}]}
        if categoria:
            filtro['$and'].append({"categoria": categoria})
        receitas_encontradas = list(receitas.find(filtro))
    return render_template('consultar_receitas.html', recipes=receitas_encontradas, consulta=consulta)

@app.route('/detalhes_receita/<id>', methods=['GET'])
def detalhes_receita(id):
    receitas = obter_colecao_receitas()
    receita = receitas.find_one({'_id': ObjectId(id)})
    return render_template('detalhes_receita.html', receita=receita)

if __name__ == '__main__':
    app.run(debug=True)
