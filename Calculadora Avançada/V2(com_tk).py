import tkinter as tk
from tkinter import ttk, messagebox
import math

# Código original fornecido pelo usuário
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

# Função principal para criar a interface
def criar_interface():
    root = tk.Tk()
    root.title("Projeto Final: Arranca Cabelo")
    root.geometry("400x300")

    # Criar e configurar o notebook (abas)
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Criar abas para cada função
    funcoes = [
        ("Adição", adicao),
        ("Subtração", subtracao),
        ("Função Quadrática", funcao_quadratica),
        ("Função Cúbica", funcao_cubica),
        ("Função Exponencial", funcao_exponencial),
        ("Exponenciação", exponenciacao),
        ("Função de Crescimento", funcao_de_crescimento),
        ("Função Hiperbólica Secante", funcao_hiperbolica_secante),
        ("Função Hiperbólica Cossecante", funcao_hiperbolica_cossecante),
        ("Função Hiperbólica Cotangente", funcao_hiperbolica_cotengente)
    ]

    for nome, funcao in funcoes:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=nome)
        criar_aba(frame, funcao)

    root.mainloop()

def criar_aba(frame, funcao):
    # Determinar os campos de entrada necessários com base na função
    campos = obter_campos(funcao)

    # Criar campos de entrada
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(frame, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5, sticky="e")
        entrada = ttk.Entry(frame)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo] = entrada

    # Criar botão de cálculo
    ttk.Button(frame, text="Calcular", command=lambda: executar_funcao(funcao, entradas)).grid(row=len(campos), column=0, columnspan=2, pady=10)

    # Criar área para exibir o resultado
    resultado_var = tk.StringVar()
    ttk.Label(frame, textvariable=resultado_var).grid(row=len(campos)+1, column=0, columnspan=2, pady=5)

    # Armazenar a variável de resultado no frame para acesso posterior
    frame.resultado_var = resultado_var

def obter_campos(funcao):
    # Mapear funções para seus campos de entrada necessários
    mapeamento_campos = {
        adicao: ["Primeiro número", "Segundo número"],
        subtracao: ["Primeiro número", "Segundo número"],
        funcao_quadratica: ["a", "b", "c"],
        funcao_cubica: ["a", "b", "c", "d"],
        funcao_exponencial: ["Base", "Expoente"],
        exponenciacao: ["Base", "Expoente"],
        funcao_de_crescimento: ["Valor inicial", "Taxa de crescimento"],
        funcao_hiperbolica_secante: ["Valor"],
        funcao_hiperbolica_cossecante: ["Valor"],
        funcao_hiperbolica_cotengente: ["Valor"]
    }
    return mapeamento_campos.get(funcao, [])

def executar_funcao(funcao, entradas):
    # Obter valores dos campos de entrada
    valores = [float(entrada.get()) for entrada in entradas.values()]

    # Executar a função e capturar o resultado
    resultado = capturar_saida(funcao, *valores)

    # Exibir o resultado
    frame = entradas[list(entradas.keys())[0]].master
    frame.resultado_var.set(resultado)

def capturar_saida(funcao, *args):
    import io
    import sys

    # Redirecionar stdout para um StringIO
    stdout_original = sys.stdout
    sys.stdout = io.StringIO()

    # Executar a função
    try:
        funcao(*args)
    except Exception as e:
        resultado = str(e)
    else:
        resultado = sys.stdout.getvalue()

    # Restaurar stdout
    sys.stdout = stdout_original

    return resultado.strip()

# Iniciar a interface
if __name__ == "__main__":
    criar_interface()