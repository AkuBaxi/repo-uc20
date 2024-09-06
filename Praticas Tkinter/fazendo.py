import tkinter as tk

def abri_segunda_tela():
    
    janelaSecundaria = tk.Toplevel()

    janelaSecundaria.title("boa tarde oooooooooo")
    

    altura= 800
    largura = 600
    janelaSecundaria.geometry(f'{largura}x{altura}')
  
    texto1 = tk.Label(janelaSecundaria, text = "segunda tela")


    botao1 = tk.Button(janelaSecundaria, text= "fechar", command= janelaSecundaria.destroy)

    texto1.place(x=350,y= 200)
    botao1.place(x=350,y= 290)

    #janelaSecundaria.mainloop()
    
    
    
janela = tk.Tk()

janela.title("bom dia")

altura = 500
largura = 500

janela.geometry(f'{largura}x{altura}')


botao = tk.Button(janela, text="oi" , command = abri_segunda_tela)

botao.place(x=100, y=100)


janela.mainloop()