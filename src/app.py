from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado em uma lista
tarefas = []
id_atual = 1

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global id_atual
    dados = request.get_json()