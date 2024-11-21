# main.py
import tkinter as tk
from tkinter import ttk
from operacoes_basicas import *
from operacoes_avancadas import *
from funcoes_especiais import *
from funcoes_hiperbolicas import *
from historico import HistoricoJanela

def obter_campos(opcao):
    mapeamento_campos = {
        "Adição": ["Primeiro número", "Segundo número"],
        "Subtração": ["Primeiro número", "Segundo número"],
        "Divisão": ["Primeiro número", "Segundo número"],
        "Função Quadrática": ["a", "b", "c"],
        "Função Cúbica": ["a", "b", "c", "d", "x"],
        "Logaritmo": ["Base", "Número"],
        "Exponenciação": ["Base", "Expoente"],
        "Função de Crescimento": ["Valor inicial", "Taxa de crescimento"],
        "Função Hiperbólica Secante": ["Valor"],
        "Função Hiperbólica Cossecante": ["Valor"],
        "Função Hiperbólica Cotangente": ["Valor"],
        "Função de Oferta": ["Preço base", "Elasticidade", "Quantidade base", "Preço atual"],
        "Função Beta": ["x", "y"]
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
        "Divisão",  # Nova função
        "Função Quadrática",
        "Função Cúbica",
        "Logaritmo",
        "Exponenciação",
        "Função de Crescimento",
        "Função Hiperbólica Secante",
        "Função Hiperbólica Cossecante",
        "Função Hiperbólica Cotangente",
        "Função de Oferta",  # Nova função
        "Função Beta"  # Nova função
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
                "Divisão": divisao,  # Nova função
                "Função Quadrática": funcao_quadratica,
                "Função Cúbica": funcao_cubica,
                "Logaritmo": logaritmo,
                "Exponenciação": exponenciacao,
                "Função de Crescimento": funcao_de_crescimento,
                "Função Hiperbólica Secante": funcao_hiperbolica_secante,
                "Função Hiperbólica Cossecante": funcao_hiperbolica_cossecante,
                "Função Hiperbólica Cotangente": funcao_hiperbolica_cotengente,
                "Função de Oferta": funcao_oferta,  # Nova função
                "Função Beta": funcao_beta  # Nova função
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

if __name__ == "__main__":
    criar_interface()