from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado em uma lista
tarefas = []
id_atual = 1

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global id_atual
    dados = request.get_json()

    # Validação obrigatória exigida no desafio
    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'O titulo e obrigatorio'}), 400

    nova_tarefa = {
        'id': id_atual,
        'titulo': dados['titulo'],
        'descricao': dados.get('descricao', ''),
        'status': dados.get('status', 'A Fazer'),
        'prazo': dados.get('prazo', None) # Incluído para a mudança de escopo
    }
    tarefas.append(nova_tarefa)
    id_atual += 1
    return jsonify(nova_tarefa), 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200