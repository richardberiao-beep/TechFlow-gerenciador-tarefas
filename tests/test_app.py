import pytest
from src.app import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

def test_criar_tarefa_com_sucesso(cliente):
    resposta = cliente.post('/tarefas', json={'titulo': 'Carregar Caminhao A'})
    assert resposta.status_code == 201
    assert resposta.json['titulo'] == 'Carregar Caminhao A'

def test_criar_tarefa_sem_titulo_deve_falhar(cliente):
    resposta = cliente.post('/tarefas', json={'descricao': 'Teste sem titulo'})
    assert resposta.status_code == 400
    assert 'erro' in resposta.json