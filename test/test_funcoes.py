# tests/test_funcoes.py
import pytest
from funcoes.funcoes import soma, dividir  # Ajustando os imports

# Teste para a função soma
def test_soma():
    assert soma(2, 3) == 5  # 2 + 3 = 5
    assert soma(-1, 1) == 0  # -1 + 1 = 0

# Teste para a função dividir
def test_dividir():
    assert dividir(10, 2) == 5  # 10 / 2 = 5
    with pytest.raises(ZeroDivisionError):  # Divisão por 0 gera um erro
        dividir(5, 0)
