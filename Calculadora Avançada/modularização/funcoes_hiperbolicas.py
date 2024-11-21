# funcoes_hiperbolicas.py
import math

def funcao_hiperbolica_secante(valor):
    try:
        resultado = 1 / math.cosh(valor)
        return f"O resultado da função hiperbólica secante é: {resultado}"
    except ZeroDivisionError:
        return "Erro: O valor não pode ser zero, pois a secante hiperbólica não é definida para esse valor."

def funcao_hiperbolica_cossecante(valor):
    if valor == 0:
        return "Erro: A função não pode ser avaliada em zero, pois a cossecante hiperbólica não é definida para esse valor."
    resultado = 1 / math.sinh(valor)
    return f"A cossecante hiperbólica de {valor} é: {resultado}"

def funcao_hiperbolica_cotengente(valor):
    try:
        resultado = math.cosh(valor) / math.sinh(valor)
        return f"O resultado da função hiperbólica cotangente é: {resultado}"
    except ZeroDivisionError:
        return "Erro: O valor não pode ser zero, pois a cotangente hiperbólica não é definida para esse valor."