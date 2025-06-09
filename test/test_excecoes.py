# tests/test_excecoes.py
import pytest
from excecoes.excecoes import converter_idade, sacar  # Ajustando os imports

# Teste para a função converter_idade
def test_converter_idade():
    assert converter_idade("30") == 30  # Conversão válida
    assert converter_idade("abc") is None  # Conversão inválida

# Teste para a função sacar
def test_sacar():
    assert sacar(100) == 100  # Valor válido
    with pytest.raises(ValueError, match="Valor negativo não é permitido"):
        sacar(-50)  # Valor negativo gera exceção
