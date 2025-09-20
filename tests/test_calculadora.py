# tests/test_calculadora.py

import pytest
from src.calculadora import somar, dividir, multiplicar, subtrair


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 1) == -1


def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(-1, 1) == -2
