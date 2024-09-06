import tkinter as tk

janela= tk.Tk()

janela.title("Ódio")

width = 500
height = 500

janela.geometry(f'{width}x{height}')

label = tk.Label (janela, text='ódio é uma palavra ruim, principalmente quando quer acabar com a vida de alguém')
label.pack()

button = tk.Button(janela, text="Clique se sente ódio")
button.pack()

button2 = tk.Button(janela, text ="a")
button2.place(x=250,y=250)

def remover_mensagem():
    button2.config(text="")

def exibir_clicado():
    button2.config(text ="Botão clicado")
    janela.after(2000, remover_mensagem)

button2.pack()


janela.mainloop()