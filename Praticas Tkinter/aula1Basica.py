#O Tkinter é uma biblioteca gráfica padrão do Python para criar interfaces gráficas de usuário (GUI). É uma ferramenta poderosa para desenvolver aplicativos com interfaces intuitivas e interativas. 
#Documentaçção 
#https://docs.python.org/pt-br/3/library/tk.html

import tkinter as tk
from tkinter import PhotoImage
from ttkthemes import ThemedStyle

# Cria uma janela principal
janela = tk.Tk()

# Define o título da janela
janela.title("Novo Título da Janela")

# Define o tamanho da janela (largura x altura)
largura = 800
altura = 600
janela.geometry(f'{largura}x{altura}')                      

# Define a janela para a tela cheia 
# largura_tela = janela.winfo_screenheight()
# altura_tela = janela.winfo_screenheight()
# janela.attributes('-topmost', True) #-alpha, -transparentcolor, -disabled, -fullscreen, -toolwindow, or -topmost
# janela.geometry(f"{largura_tela}x{altura_tela}+0+0")

# # Define o caminho para o arquivo de ícone (.ico, .png, etc.)
# caminho_icone = "img/cash.ico"

# # Define o ícone da janela
# janela.iconbitmap(caminho_icone)

#adiciona um rótulo á janela
label = tk.Label(janela, text="ola, Tlinter!")
label.pack()

#Adiciona um botão a janela
botao = tk.Button(janela, text="Clique aqui")
botao.pack()

#Adiciona um campo de texto
texto = tk.Entry(janela)
texto.pack()

#Adiciona uma caixa de seleção de texto á jenela 
opcao1 = tk.Checkbutton(janela, text="Opção 1 caixa de seleção")
opcao2 = tk.Checkbutton(janela, text="Opção 2 caixa de seleção")
opcao1.pack()
opcao2.pack()

#Adicona uma caixa de opçães á janela
opcao1 = tk.Radiobutton(janela, text="Opção 1 Caixa de Opções", value=1)
opcao2 = tk.Radiobutton(janela, text="Opção 2 Caixa de Opções", value=2)
opcao1.pack()
opcao2.pack()


#Adiciona uma Área de texto á janela
text = tk.Text(janela)
text.pack()

#Adiciona um frame á jenela
frame = tk.Frame(janela)
frame.pack()

def funcao_sair():
    janela.quit()

#cria um menu
menu = tk.Menu(janela)
janela.config(menu=menu)

#cria um menu "Arquivo" com uma opção "sair"
menu_arquivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=funcao_sair)

# Cria um menu "Configurações" com uma opção "Nada, Nada2"
menu_config = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Configurações", menu=menu_config)
menu_config.add_command(label="Nada", command="")
menu_config.add_command(label="Nada2",command="")


janela.mainloop()