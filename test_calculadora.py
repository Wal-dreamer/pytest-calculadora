import pytest
from calculadora import CalculadoraService

def test_somar_dois_positivos():
    calc = CalculadoraService()
    assert calc.somar(2, 3) == 5

def test_somar_positivo_e_negativo():
    calc = CalculadoraService()
    assert calc.somar(5, -2) == 3

def test_somar_dois_zeros():
    calc = CalculadoraService()
    assert calc.somar(0, 0) == 0

# Testes para subtrair
def test_subtrair_corretamente():
    calc = CalculadoraService()
    assert calc.subtrair(10, 5) == 5

def test_subtrair_resultado_negativo():
    calc = CalculadoraService()
    assert calc.subtrair(5, 10) == -5

def test_subtrair_valores_iguais():
    calc = CalculadoraService()
    assert calc.subtrair(5, 5) == 0

# Testes para multiplicar
def test_multiplicar_dois_positivos():
    calc = CalculadoraService()
    assert calc.multiplicar(2, 3) == 6

def test_multiplicar_por_zero():
    calc = CalculadoraService()
    assert calc.multiplicar(5, 0) == 0

def test_multiplicar_negativos():
    calc = CalculadoraService()
    assert calc.multiplicar(-2, 3) == -6

# Testes para dividir
def test_dividir_quociente_correto():
    calc = CalculadoraService()
    assert calc.dividir(10, 2) == 5

def test_dividir_por_zero():
    calc = CalculadoraService()
    with pytest.raises(ValueError, match="Divisão por zero não permitida"):
        calc.dividir(10, 0)

def test_dividir_decimais():
    calc = CalculadoraService()
    assert calc.dividir(5, 2) == 2.5

# Testes para isPar
def test_is_par_verdadeiro():
    calc = CalculadoraService()
    assert calc.isPar(4) is True

def test_is_par_falso():
    calc = CalculadoraService()
    assert calc.isPar(7) is False

def test_is_par_zero():
    calc = CalculadoraService()
    assert calc.isPar(0) is True

# Testes para validarNumeroPositivo
def test_validar_positivo_verdadeiro():
    calc = CalculadoraService()
    assert calc.validarNumeroPositivo(10) is True

def test_validar_positivo_falso():
    calc = CalculadoraService()
    assert calc.validarNumeroPositivo(-5) is False

def test_validar_positivo_zero():
    calc = CalculadoraService()
    # Definindo regra: zero não é positivo (comum em matemática, mas depende da regra de negócio)
    assert calc.validarNumeroPositivo(0) is False
