# operacoes_avancadas.py
import math

def funcao_quadratica(a, b, c):
    d = (b**2) - (4*a*c)
    if d < 0:
        return "A equação não tem raízes reais."
    elif d == 0:
        raiz = -b / (2 * a)
        return f"A equação tem uma raiz real: {raiz}"
    else:
        raiz1 = (-b + d**0.5) / (2 * a)
        raiz2 = (-b - d**0.5) / (2 * a)
        return f"A equação tem duas raízes reais: {raiz1} e {raiz2}"

def funcao_cubica(a, b, c, d, x):
    if a == 0:
        return "O valor de 'a' não pode ser zero em uma equação cúbica."
    
    resultado = a * x**3 + b * x**2 + c * x + d
    
    b_a = b / a
    c_a = c / a
    d_a = d / a
    delta = 18 * b_a * c_a * d_a - 4 * b_a**3 * d_a + b_a**2 * c_a**2 - 4 * c_a**3 - 27 * d_a**2
    
    if delta > 0:
        raizes = "três raízes reais distintas"
    elif delta == 0:
        raizes = "uma raiz real dupla e uma simples"
    else:
        raizes = "uma raiz real e duas complexas"
    
    return f"Para x = {x}, o valor da função cúbica é: {resultado}\n" \
            f"A equação cúbica tem {raizes}."

def funcao_de_crescimento(valor_inicial, taxa_de_crescimento):
    if valor_inicial < 0 or taxa_de_crescimento < 0:
        return "Os valores devem ser não-negativos."
    resultado = valor_inicial * taxa_de_crescimento
    return f"O resultado do crescimento é: {resultado}"

def funcao_oferta(preco_base, elasticidade, quantidade_base):
    """
    Calcula a função de oferta linear
    Q = quantidade_base + elasticidade * (P - preco_base)
    onde Q é a quantidade ofertada e P é o preço
    """
    def calcular_oferta(preco):
        quantidade = quantidade_base + elasticidade * (preco - preco_base)
        return max(0, quantidade)  # A quantidade não pode ser negativa
    
    return calcular_oferta