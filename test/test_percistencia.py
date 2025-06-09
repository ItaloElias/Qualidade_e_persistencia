import os
import json
from persistencia import ler_pontuacoes, salvar_pontuacao_json

# Teste para ler pontuações de um arquivo vazio
def test_ler_pontuacoes_vazio():
    # Remover arquivos residuais antes do teste
    if os.path.exists('pontuacoes.txt'):
        os.remove('pontuacoes.txt')
    
    pontuacoes = ler_pontuacoes()
    assert pontuacoes == []

# Teste para salvar pontuação em arquivo JSON
def test_salvar_pontuacao_json():
    # Remover arquivos residuais antes do teste
    if os.path.exists('pontuacoes.json'):
        os.remove('pontuacoes.json')
    
    salvar_pontuacao_json('Alice', 10)
    salvar_pontuacao_json('Bob', 15)
    
    # Verificando se o arquivo JSON foi criado corretamente
    with open('pontuacoes.json', 'r') as arquivo:
        pontuacoes = json.load(arquivo)
    
    assert len(pontuacoes) == 2
    assert pontuacoes[0] == {'nome': 'Alice', 'pontos': 10}
    assert pontuacoes[1] == {'nome': 'Bob', 'pontos': 15}