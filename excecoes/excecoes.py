# excecoes/excecoes.py

# Função para converter idade
def converter_idade(texto):
    try:
        return int(texto)
    except ValueError:
        return None

# Função sacar com exceção personalizada
def sacar(valor):
    if valor < 0:
        raise ValueError("Valor negativo não é permitido")
    return valor
