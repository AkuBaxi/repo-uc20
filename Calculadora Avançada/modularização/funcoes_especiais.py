# funcoes_especiais.py
import math

def logaritmo(base, numero):
    if base <= 0 or base == 1:
        raise ValueError("A base deve ser maior que 0 e diferente de 1.")    
    if numero <= 0:
        raise ValueError("O número deve ser maior que 0.")
    resultado = math.log(numero, base)
    return f"O resultado é {resultado}"

def exponenciacao(base, expoente):
    if base == 0 and expoente < 0:
        return "A base não pode ser zero e o expoente deve ser positivo."
    resultado = base ** expoente
    return f"O resultado é {resultado}"

def funcao_beta(x, y):
    """
    Calcula a função beta B(x,y) = Γ(x)Γ(y)/Γ(x+y)
    onde Γ é a função gamma
    """
    if x <= 0 or y <= 0:
        return "Erro: Os parâmetros devem ser positivos"
    try:
        resultado = math.gamma(x) * math.gamma(y) / math.gamma(x + y)
        return f"O valor da função beta B({x},{y}) é: {resultado}"
    except OverflowError:
        return "Erro: Valores muito grandes para cálculo"