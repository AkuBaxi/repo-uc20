import tkinter as tk
from tkinter import ttk, messagebox
import math

# Adição (Fácil) - 1
def adicao(num1, num2):
    return f"A soma dos dois números é: {num1 + num2}"

# Subtração (Fácil) - 2
def subtracao(num1, num2):
    return f"A subtração dos dois números é: {num1 - num2}"

# Função Quadrática (Média) - 9
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

# Função Cúbica (Média) - 10
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

# Logaritmo (Média) - 7
def logaritmo(base,numero):
        resultado = math.log(numero, base)
        if base <= 0 or base == 1:
            raise ValueError("A base deve ser maior que 0 e diferente de 1.")    
        if numero <= 0:
            raise ValueError("O número deve ser maior que 0.")
        return f"O resultado é {resultado}"



# Exponenciação (Média) - 5
def exponenciacao(base, expoente):
    if base == 0 and expoente < 0:
        return "A base não pode ser zero e o expoente deve ser positivo."
    resultado = base ** expoente
    return f"O resultado é {resultado}"


# Função de Crescimento (Média) - 39
def funcao_de_crescimento(valor_inicial, taxa_de_crescimento):
    if valor_inicial < 0 or taxa_de_crescimento < 0:
        return "Os valores devem ser não-negativos."
    resultado = valor_inicial * taxa_de_crescimento
    return f"O resultado do crescimento é: {resultado}"

# Função Hiperbólica Secante (Difícil) - 26
def funcao_hiperbolica_secante(valor):
    try:
        resultado = 1 / math.cosh(valor)
        return f"O resultado da função hiperbólica secante é: {resultado}"
    except ZeroDivisionError:
        return "Erro: O valor não pode ser zero, pois a secante hiperbólica não é definida para esse valor."
    

# Função Hiperbólica Cossecante (Difícil) - 27
def funcao_hiperbolica_cossecante(valor):
    if valor == 0:
        return "Erro: A função não pode ser avaliada em zero, pois a cossecante hiperbólica não é definida para esse valor."
    resultado = 1 / math.sinh(valor)
    return f"A cossecante hiperbólica de {valor} é: {resultado}"


# Função Hiperbólica Cotangente (Difícil) - 28
def funcao_hiperbolica_cotengente(valor):
    try:
        resultado = math.cosh(valor) / math.sinh(valor)
        return f"O resultado da função hiperbólica cotangente é: {resultado}"
    except ZeroDivisionError:
        return "Erro: O valor não pode ser zero, pois a cotangente hiperbólica não é definida para esse valor."
# Nova classe para a janela de histórico
class HistoricoJanela:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Histórico de Operações")
        self.window.geometry("400x500")
        
        # Criar frame principal
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Adicionar scrollbar
        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Empacotar widgets
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def atualizar_historico(self, historico):
        # Limpar frame atual
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Adicionar cada operação ao histórico
        for operacao in historico:
            # Frame para cada operação
            op_frame = ttk.Frame(self.scrollable_frame)
            op_frame.pack(fill=tk.X, padx=5, pady=5)
            
            # Labels para a operação e resultado
            ttk.Label(op_frame, text=operacao['operacao'], font=('Arial', 10, 'bold')).pack(anchor='w')
            ttk.Label(op_frame, text=operacao['resultado'], wraplength=350).pack(anchor='w', padx=(10, 0))
            
            # Linha separadora
            ttk.Separator(self.scrollable_frame, orient='horizontal').pack(fill=tk.X, padx=5, pady=5)

        # Atualizar a região de rolagem após adicionar novos widgets
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
def obter_campos(opcao):
    mapeamento_campos = {
        "Adição": ["Primeiro número", "Segundo número"],
        "Subtração": ["Primeiro número", "Segundo número"],
        "Função Quadrática": ["a", "b", "c"],
        "Função Cúbica": ["a", "b", "c", "d", "x"],
        "Logaritmo": ["Base", "Número"],
        "Exponenciação": ["Base", "Expoente"],
        "Função de Crescimento": ["Valor inicial", "Taxa de crescimento"],
        "Função Hiperbólica Secante": ["Valor"],
        "Função Hiperbólica Cossecante": ["Valor"],
        "Função Hiperbólica Cotangente": ["Valor"]
    }
    return mapeamento_campos.get(opcao, [])

def criar_interface():
    root = tk.Tk()
    root.title("Projeto Final: Arranca Cabelo")
    root.geometry("500x400")

    # Lista para armazenar o histórico
    historico = []
    
    # Variável para armazenar a referência da janela de histórico
    historico_janela = None

    def abrir_historico():
        nonlocal historico_janela
        if historico_janela is None or not historico_janela.window.winfo_exists():
            historico_janela = HistoricoJanela(root)
        historico_janela.atualizar_historico(historico)
        historico_janela.window.lift()

    # Frame para o botão de histórico
    top_frame = ttk.Frame(root)
    top_frame.pack(fill=tk.X, padx=10, pady=5)
    
    # Botão de histórico
    historico_btn = ttk.Button(top_frame, text="Histórico", command=abrir_historico)
    historico_btn.pack(side=tk.RIGHT)

    # Criar frame principal
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Criar lista de opções
    opcoes = [
        "Adição",
        "Subtração",
        "Função Quadrática",
        "Função Cúbica",
        "Logaritmo",
        "Exponenciação",
        "Função de Crescimento",
        "Função Hiperbólica Secante",
        "Função Hiperbólica Cossecante",
        "Função Hiperbólica Cotangente"
    ]

    # Variável para armazenar a opção selecionada
    opcao_selecionada = tk.StringVar()

    # Criar combobox para seleção de opções
    ttk.Label(main_frame, text="Escolha uma operação:").pack(pady=5)
    combo = ttk.Combobox(main_frame, textvariable=opcao_selecionada, values=opcoes, state="readonly")
    combo.pack(pady=5)
    combo.bind("<<ComboboxSelected>>", lambda _: atualizar_campos(opcao_selecionada.get(), main_frame))

    def calcular_com_historico(opcao, entradas, main_frame):
        try:
            valores = [float(entrada.get()) for entrada in entradas.values()]
            funcoes = {
                "Adição": adicao,
                "Subtração": subtracao,
                "Função Quadrática": funcao_quadratica,
                "Função Cúbica": funcao_cubica,
                "Logaritmo": logaritmo,
                "Exponenciação": exponenciacao,
                "Função de Crescimento": funcao_de_crescimento,
                "Função Hiperbólica Secante": funcao_hiperbolica_secante,
                "Função Hiperbólica Cossecante": funcao_hiperbolica_cossecante,
                "Função Hiperbólica Cotangente": funcao_hiperbolica_cotengente
            }
            resultado = funcoes[opcao](*valores)
            main_frame.resultado_var.set(resultado)
            
            # Adicionar ao histórico
            historico.append({
                'operacao': opcao,
                'resultado': resultado
            })
            
            # Atualizar janela de histórico se estiver aberta
            if historico_janela is not None and historico_janela.window.winfo_exists():
                historico_janela.atualizar_historico(historico)
                
        except ValueError:
            main_frame.resultado_var.set("Erro: Por favor, insira valores numéricos válidos.")
        except Exception as e:
            main_frame.resultado_var.set(f"Erro: {str(e)}")

    def atualizar_campos(opcao, main_frame):
        # Limpar campos existentes
        for widget in main_frame.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.destroy()

        # Criar novos campos de entrada
        campos_frame = ttk.Frame(main_frame)
        campos_frame.pack(pady=10, fill=tk.X)

        campos = obter_campos(opcao)
        entradas = {}
        for campo in campos:
            frame = ttk.Frame(campos_frame)
            frame.pack(fill=tk.X, pady=2)
            ttk.Label(frame, text=f"{campo}:").pack(side=tk.LEFT)
            entrada = ttk.Entry(frame)
            entrada.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
            entradas[campo] = entrada

        # Criar botão de cálculo
        ttk.Button(campos_frame, text="Calcular", 
                command=lambda: calcular_com_historico(opcao, entradas, main_frame)).pack(pady=10)

        # Criar área para exibir o resultado
        resultado_frame = ttk.Frame(main_frame)
        resultado_frame.pack(pady=10, fill=tk.X)
        resultado_var = tk.StringVar()
        ttk.Label(resultado_frame, textvariable=resultado_var, wraplength=400).pack()

        # Armazenar a variável de resultado no frame para acesso posterior
        main_frame.resultado_var = resultado_var

    root.mainloop()

# Iniciar a interface
if __name__ == "__main__":
    criar_interface()
