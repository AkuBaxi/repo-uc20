import tkinter as tk
from tkinter import Menu, PhotoImage
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys, os


janela = tk.Tk()

estilo = ThemedStyle(janela)
estilo.set_theme("arc")

janela.title = ("solo")

largura = 800
altura = 600
janela.geometry(f'{largura}x{altura}')

program_directory=sys.path[0]
janela.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "img/aiko_icon.png")))


label = ttk.Label(janela, text="texto")
label.pack()

botao = ttk.Button(janela, text="caixa") 
botao.pack()

entrada = ttk.Entry(janela)
entrada.pack()

opcao = ttk.Checkbutton(janela, text="opcao 1")
opcao.pack()


opcao1 = ttk.Radiobutton(janela, text = "opcao 1", value=1)
opcao1.pack

texto = tk.Text(janela)
texto.pack()

def funcao_sair():
    janela.quit

menu = tk.Menu(janela)
janela.config(menu=menu)

menu_arquivo = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="sair", command=funcao_sair)

menu_config = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="configuração", menu=menu_arquivo)
menu_config.add_command(label="nada", command="")
menu_config.add_command(label="nada2", command="")

imagem = PhotoImage(file="img/aiko_icon.png")


janela.mainloop()
