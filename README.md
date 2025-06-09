# Qualidade de Código e Persistência de Dados

Este repositório contém um projeto de exemplo para demonstração de práticas de qualidade de código, testes automatizados com `pytest` e persistência de dados utilizando arquivos e JSON.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
projeto/
│
├── funcoes/
│   ├── __init__.py      # Arquivo que define o pacote 'funcoes'
│   └── funcoes.py       # Funções de exemplo (ex.: soma, dividir)
│
├── excecoes/
│   ├── __init__.py      # Arquivo que define o pacote 'excecoes'
│   └── excecoes.py      # Funções para tratamento de exceções (ex.: converter_idade, sacar)
│
├── persistencia/
│   ├── __init__.py      # Arquivo que define o pacote 'persistencia'
│   └── persistencia.py  # Funções para persistir dados (ex.: salvar pontuação)
│
├── tests/
│   ├── test_funcoes.py         # Testes para o pacote 'funcoes'
│   ├── test_excecoes.py        # Testes para o pacote 'excecoes'
│   └── test_persistencia.py    # Testes para o pacote 'persistencia'
│
├── requirements.txt            # Arquivo de dependências do projeto
└── README.md                   # Este arquivo
```

## Requisitos

Antes de rodar o projeto, é necessário ter o Python 3.x instalado na sua máquina. Você pode verificar sua versão do Python com:

```bash
python --version
```

Além disso, você vai precisar de um ambiente virtual para instalar as dependências isoladas.

## Configuração do Ambiente Virtual

Para começar, crie um ambiente virtual dentro da pasta do projeto:

### Passos para criar e ativar o ambiente virtual:

1. **Crie o ambiente virtual**:

   ```bash
   python -m venv venv
   ```

2. **Ative o ambiente virtual**:

   * No **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```

   * No **Linux/Mac**:

     ```bash
     source venv/bin/activate
     ```

Você deve ver `(venv)` no início da linha de comando, o que indica que o ambiente virtual está ativo.

## Instalando as Dependências

Com o ambiente virtual ativo, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja presente ou precise ser gerado, siga os passos abaixo:

```bash
pip freeze > requirements.txt
```

## Rodando os Testes

Os testes automatizados do projeto estão implementados usando `pytest`. Para rodar os testes:

```bash
pytest
```

### Estrutura dos Testes

* `test_funcoes.py`: Testes para funções de soma e divisão.
* `test_excecoes.py`: Testes para exceções como `ZeroDivisionError` e entradas inválidas.
* `test_persistencia.py`: Testes para persistência de dados (salvar e ler pontuação).

### Exemplo de Saída

```
=============================== test session starts ================================
platform win32 -- Python 3.x.x, pytest-8.x.x, pluggy-1.x.x
rootdir: C:\Users\Aluno\Documents\Qualidade_codigo_persistente
collected 6 items

test/test_excecoes.py ..                                                      [ 33%]
test/test_funcoes.py ..                                                       [ 66%]
test/test_percistencia.py ..                                                  [100%]

================================ 6 passed in 0.10s =================================
```

## Persistência de Dados

Funções principais:

* `salvar_pontuacao(nome, pontos)`
* `ler_pontuacoes()`
* `salvar_pontuacao_json(nome, pontos)`

### Exemplo:

```python
salvar_pontuacao("Alice", 100)
pontuacoes = ler_pontuacoes()
print(pontuacoes)
```

## Tratamento de Exceções

Exemplos:

```python
idade = converter_idade("20")
valor = sacar(100)
```

## Contribuindo

Faça um fork, crie uma branch, implemente as alterações e envie um pull request.

## Licença

Projeto open-source para fins educacionais e comunitários.
