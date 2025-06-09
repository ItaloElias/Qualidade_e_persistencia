# persistencia/persistencia.py
import json

# Função de salvar pontuação em arquivo de texto
def salvar_pontuacao(nome, pontos):
    with open('pontuacoes.txt', 'a') as arquivo:
        arquivo.write(f"{nome},{pontos}\n")

# Função de ler pontuações do arquivo de texto
def ler_pontuacoes():
    try:
        with open('pontuacoes.txt', 'r') as arquivo:
            return [tuple(line.strip().split(',')) for line in arquivo]
    except FileNotFoundError:
        return []

# Função de salvar pontuação em arquivo JSON
def salvar_pontuacao_json(nome, pontos):
    try:
        with open('pontuacoes.json', 'r') as arquivo:
            pontuacoes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        pontuacoes = []

    pontuacoes.append({"nome": nome, "pontos": pontos})

    with open('pontuacoes.json', 'w') as arquivo:
        json.dump(pontuacoes, arquivo, indent=4)

# Função para adicionar uma nova pontuação
def adicionar_pontuacao(nome, pontos):
    salvar_pontuacao_json(nome, pontos)
