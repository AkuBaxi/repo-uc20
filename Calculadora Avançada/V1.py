import math

# Adição (Fácil) - 1
def adicao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A soma dos dois números é: {num1 + num2}")
    except  ValueError:
        print("!") 
        # Mudar depois


# Subtração (Fácil) - 2
def  subtracao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A subtração dos dois números é: {num1 - num2}")
    except ValueError:
        print("!")
        # Mudar depois
    

# Função Quadrática (Média) - 9
def funcao_quadratica():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        
        d = (b**2) - (4*a*c)
        
        if d < 0:
            print("A equação não tem raízes reais.")
        elif d == 0:
            raiz = -b / (2 * a)
            print(f"A equação tem uma raiz real: {raiz}")
        else:
            raiz1 = (-b + d**0.5) / (2 * a)
            raiz2 = (-b - d**0.5) / (2 * a)
            print(f"A equação tem duas raízes reais: {raiz1} e {raiz2}")
    except ValueError:
        print("Por favor, insira números válidos.")
    except ZeroDivisionError:
        print("O coeficiente 'a' não pode ser zero.")


# Função Cúbica (Média) - 10
def funcao_cubica():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        d = float(input("Digite o valor de d: "))

        if a == 0:
            print("O valor de 'a' não pode ser zero em uma equação cúbica.")
            return

        b /= a
        c /= a
        d /= a
        delta = 18 * b * c * d - 4 * b**3 * d + b**2 * c**2 - 4 * c**3 - 27 * d**2
        if delta > 0:
            print("A equação cúbica tem três raízes reais distintas.")
            
        elif delta == 0:
            print("A equação cúbica tem uma raiz real dupla e uma simples.")
        else:
            print("A equação cúbica tem uma raiz real e duas complexas.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# VER AINDA PQ É IGUAL
# Função Exponencial (Média) - 11
def funcao_exponencial():
    try:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))

        if base == 0:
            print("A base não pode ser zero.")
            return

        if not isinstance(expoente, (int, float)):
            print("O expoente deve ser um número real.")
            return
        elif expoente == 0:
            print("O resultado é 1.")
        elif expoente < 0:
            print("O resultado é 0.")
        else:
            print("O resultado é {:.2f}.".format(base ** expoente))

        resultado = base ** expoente
        print(f"O resultado da função exponencial é: {resultado}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


# Exponenciação (Média) - 5
def exponenciacao():
    try:
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        if base == 0 and expoente < 0:
            print("A base não pode ser zero e o expoente deve ser positivo.")
            return
        elif base == 0 and expoente >= 0:
            print("O resultado é 0.")
        elif base != 0 and expoente < 0:
            print("O resultado é 0.")
        else:
            print("O resultado é {:.2f}.".format(base ** expoente))
        resultado = base ** expoente
        print(f"O resultado da função exponencial é: {resultado}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
# IGUAL

# Função de Crescimento (Média) - 39
def funcao_de_crescimento():
    try:
        valor_inicial = float(input("Digite o valor inicial: "))
        taxa_de_crescimento = float(input("Digite a taxa de crescimento: "))
        
        if valor_inicial < 0 or taxa_de_crescimento < 0:
            raise ValueError("Os valores devem ser não-negativos.")
        
        resultado = valor_inicial * taxa_de_crescimento
        print(f"O resultado do crescimento é: {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")


# Função Hiperbólica Secante (Difícil) - 26
def funcao_hiperbolica_secante():
    try:
        valor = float(input("Digite o valor: "))
        
        resultado = 1 / math.cosh(valor)
        print(f"O resultado da função hiperbólica secante é: {resultado}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        print("Erro: O valor não pode ser zero, pois a secante hiperbólica não é definida para esse valor.")


# Função Hiperbólica Cossecante (Difícil) - 27
import math

def funcao_hiperbolica_cossecante():
    try:
        valor = float(input("Digite um número para calcular a cossecante hiperbólica: "))
        
        if valor == 0:
            raise ZeroDivisionError("Erro: A função não pode ser avaliada em zero, pois a cossecante hiperbólica não é definida para esse valor.")
        
        resultado = 1 / math.sinh(valor)
        print(f"A cossecante hiperbólica de {valor} é: {resultado}")
    
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")



# Função Hiperbólica Cotangente (Difícil) - 28
def funcao_hiperbolica_cotengente():
    try:
        valor = float(input("Digite o valor: "))
        
        if math.sinh(valor) == 0:
            raise ZeroDivisionError 

        resultado = math.cosh(valor) / math.sinh(valor)
        print(f"O resultado da função hiperbólica cotangente é: {resultado}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
    except ZeroDivisionError:
        print("Erro: O valor não pode ser zero, pois a cotangente hiperbólica não é definida para esse valor.")

def menu_principal():
    """Exibe o menu principal e gerencia a seleção do usuário"""
    while True:
        print("\n=== Arranca Cabelo ===")
        print("\nEscolha um tipo de operação matemática que deseja fazer:")
        print("1. Adição)")
        print("2. Subtração)")
        print("3. Função Quadrática)")
        print("4. Função Cúbica)")
        print("5. Função Exponencial)")
        print("6. Exponenciação)")
        print("7. Função de Crescimento)")
        print("8. Função Hiperbólica Secante)")
        print("9. Função Hiperbólica Cossecante")
        print("10. Função Hiperbólica Cotangente")
        print("0. Sair")

        try:
            opcao = int(input("\nDigite o número da opção desejada: "))
            
            if opcao == 0:
                print("\nEncerrando o programa...")
                break
                
            funcoes = {
                1: adicao,
                2: subtracao,
                3: funcao_quadratica,
                4: funcao_cubica,
                5: funcao_exponencial,
                6: exponenciacao,
                7: funcao_de_crescimento,
                8: funcao_hiperbolica_secante,
                9: funcao_hiperbolica_cossecante,
                10: funcao_hiperbolica_cotengente
            }
            
            if opcao in funcoes:
                funcoes[opcao]()
                input("\nPressione ENTER para continuar...")
            else:
                print("\nOpção inválida! Por favor, escolha um número entre 0 e 10.")
                
        except ValueError:
            print("\nPor favor, digite apenas números!")

if __name__ == "__main__":
    menu_principal()