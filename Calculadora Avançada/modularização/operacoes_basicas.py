# operacoes_basicas.py
def adicao(num1, num2):
    return f"A soma dos dois números é: {num1 + num2}"

def subtracao(num1, num2):
    return f"A subtração dos dois números é: {num1 - num2}"

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida"
    return f"A divisão dos dois números é: {num1 / num2}"