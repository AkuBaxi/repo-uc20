import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from PIL import Image, ImageTk

# Dicionário de regras gramaticais (exemplo)
regras_gramaticais = {
    "Uso do acento agudo": "O acento agudo é utilizado...",
    "Emprego da crase": "A crase ocorre...",
    "Uso dos pronomes relativos": "Os pronomes relativos...",
    # Adicione mais regras gramaticais conforme necessário
}

class PerfilUsuario:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.foto_perfil = None
        self.favoritos = []

    def adicionar_favorito(self, regra):
        if regra not in self.favoritos:
            self.favoritos.append(regra)

    def remover_favorito(self, regra):
        if regra in self.favoritos:
            self.favoritos.remove(regra)

    def editar_nome(self, novo_nome):
        self.nome_usuario = novo_nome

    def carregar_foto_perfil(self, caminho_foto):
        try:
            self.foto_perfil = Image.open(caminho_foto)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar foto: {str(e)}")

    def obter_foto_perfil(self):
        if self.foto_perfil:
            return ImageTk.PhotoImage(self.foto_perfil)
        else:
            return None

class AplicativoGramaticaMobile:
    def __init__(self, root, perfil):
        self.root = root
        self.perfil = perfil
        self.root.title("Aplicativo de Gramática")
        self.root.geometry("360x640")  # Dimensões típicas do Samsung A20 (360x640 pixels)

        # Frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Frame para a lista de regras gramaticais
        self.frame_regras = tk.Frame(self.frame_principal)
        self.frame_regras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Lista de regras gramaticais
        self.lista_regras = tk.Listbox(self.frame_regras, selectmode=tk.SINGLE)
        self.lista_regras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar para a lista de regras
        scrollbar = tk.Scrollbar(self.frame_regras)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_regras.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_regras.yview)
        
        # Adicionar regras gramaticais à lista
        for regra in regras_gramaticais:
            self.lista_regras.insert(tk.END, regra)
        
        # Frame para detalhes da regra selecionada
        self.frame_detalhes = tk.Frame(self.frame_principal)
        self.frame_detalhes.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Texto de detalhes da regra
        self.texto_detalhes = tk.Text(self.frame_detalhes, wrap=tk.WORD)
        self.texto_detalhes.pack(fill=tk.BOTH, expand=True)
        
        # Frame para o perfil do usuário
        self.frame_perfil = tk.Frame(self.root)
        self.frame_perfil.pack(pady=10, fill=tk.BOTH)

        # Botão para visualizar perfil
        self.botao_perfil = tk.Button(self.frame_perfil, text="Ver Meu Perfil", command=self.visualizar_perfil)
        self.botao_perfil.pack(side=tk.LEFT, padx=10)

        # Entrada de busca
        self.entrada_busca = tk.Entry(self.frame_perfil, width=20)
        self.entrada_busca.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Botão para buscar
        self.botao_buscar = tk.Button(self.frame_perfil, text="Buscar", command=self.buscar_regra)
        self.botao_buscar.pack(side=tk.LEFT, padx=10)

        # Configurar evento de seleção na lista
        self.lista_regras.bind('<<ListboxSelect>>', self.mostrar_detalhes_regra)

    def mostrar_detalhes_regra(self, event):
        # Obter o índice da regra selecionada
        index = self.lista_regras.curselection()
        if index:
            regra_selecionada = self.lista_regras.get(index)
            detalhes = regras_gramaticais.get(regra_selecionada, "Detalhes não disponíveis.")
            self.texto_detalhes.delete('1.0', tk.END)
            self.texto_detalhes.insert(tk.END, detalhes)

    def visualizar_perfil(self):
        # Destruir frame principal para ocultar
        self.frame_principal.destroy()

        # Criar novo frame para visualização do perfil
        perfil_frame = tk.Frame(self.root)
        perfil_frame.pack(fill=tk.BOTH, expand=True)

        # Nome do usuário
        label_nome = tk.Label(perfil_frame, text=f"Nome de usuário: {self.perfil.nome_usuario}")
        label_nome.pack(pady=10)

        # Foto de perfil
        foto_perfil = self.perfil.obter_foto_perfil()
        if foto_perfil:
            label_foto = tk.Label(perfil_frame, image=foto_perfil)
            label_foto.pack()
            label_foto.image = foto_perfil  # Manter referência para evitar garbage collection
        else:
            label_sem_foto = tk.Label(perfil_frame, text="Foto de perfil não definida.")
            label_sem_foto.pack()

        # Botão para editar perfil
        botao_editar = tk.Button(perfil_frame, text="Editar Perfil", command=self.editar_perfil)
        botao_editar.pack(pady=10)

        # Botão para voltar à tela anterior
        botao_voltar = tk.Button(perfil_frame, text="Voltar", command=lambda: self.recriar_frame_principal(perfil_frame))
        botao_voltar.pack(pady=10)

    def editar_perfil(self):
        # Destruir frame principal para ocultar
        self.frame_principal.destroy()

        # Criar novo frame para edição de perfil
        editar_frame = tk.Frame(self.root)
        editar_frame.pack(fill=tk.BOTH, expand=True)

        # Label e entrada para novo nome
        label_novo_nome = tk.Label(editar_frame, text="Novo nome de usuário:")
        label_novo_nome.pack(pady=10)
        entry_novo_nome = tk.Entry(editar_frame)
        entry_novo_nome.pack()

        # Botão para escolher foto
        botao_escolher_foto = tk.Button(editar_frame, text="Escolher Foto", command=self.escolher_foto)
        botao_escolher_foto.pack(pady=10)

        # Botão para salvar alterações
        botao_salvar = tk.Button(editar_frame, text="Salvar", command=lambda: self.salvar_perfil(entry_novo_nome.get(), editar_frame))
        botao_salvar.pack(pady=10)

        # Botão para voltar à tela anterior
        botao_voltar = tk.Button(editar_frame, text="Voltar", command=lambda: self.recriar_frame_principal(editar_frame))
        botao_voltar.pack(pady=10)

    def recriar_frame_principal(self, frame_atual):
        # Destruir frame atual e recriar frame principal
        frame_atual.destroy()
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        # Recriar componentes da tela principal
        self.frame_regras = tk.Frame(self.frame_principal)
        self.frame_regras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.lista_regras = tk.Listbox(self.frame_regras, selectmode=tk.SINGLE)
        self.lista_regras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(self.frame_regras)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_regras.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lista_regras.yview)
        
        for regra in regras_gramaticais:
            self.lista_regras.insert(tk.END, regra)
        
        self.frame_detalhes = tk.Frame(self.frame_principal)
        self.frame_detalhes.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.texto_detalhes = tk.Text(self.frame_detalhes, wrap=tk.WORD)
        self.texto_detalhes.pack(fill=tk.BOTH, expand=True)

        self.frame_perfil = tk.Frame(self.root)
        self.frame_perfil.pack(pady=10, fill=tk.BOTH)

        self.botao_perfil = tk.Button(self.frame_perfil, text="Ver Meu Perfil", command=self.visualizar_perfil)
        self.botao_perfil.pack(side=tk.LEFT, padx=10)

        self.entrada_busca = tk.Entry(self.frame_perfil, width=20)
        self.entrada_busca.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        self.botao_buscar = tk.Button(self.frame_perfil, text="Buscar", command=self.buscar_regra)
        self.botao_buscar.pack(side=tk.LEFT, padx=10)

        self.lista_regras.bind('<<ListboxSelect>>', self.mostrar_detalhes_regra)

    def escolher_foto(self):
        caminho_foto = filedialog.askopenfilename(filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg")])
        if caminho_foto:
            self.perfil.carregar_foto_perfil(caminho_foto)

    def salvar_perfil(self, novo_nome, frame_atual):
        self.perfil.editar_nome(novo_nome)
        messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso.")
        self.recriar_frame_principal(frame_atual)

    def buscar_regra(self):
        termo_busca = self.entrada_busca.get().strip()
        if termo_busca:
            self.lista_regras.delete(0, tk.END)
            
            for regra in regras_gramaticais:
                if termo_busca.lower() in regra.lower():
                    self.lista_regras.insert(tk.END, regra)

    def run(self):
        self.root.mainloop()

# Função principal para iniciar o aplicativo
if __name__ == "__main__":
    nome_usuario = "Usuário"
    perfil = PerfilUsuario(nome_usuario)

    root = tk.Tk()
    app = AplicativoGramaticaMobile(root, perfil)
    app.run()
