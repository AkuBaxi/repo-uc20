# historico.py
import tkinter as tk
from tkinter import ttk

class HistoricoJanela:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Histórico de Operações")
        self.window.geometry("400x500")
        
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def atualizar_historico(self, historico):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for operacao in historico:
            op_frame = ttk.Frame(self.scrollable_frame)
            op_frame.pack(fill=tk.X, padx=5, pady=5)
            
            ttk.Label(op_frame, text=operacao['operacao'], font=('Arial', 10, 'bold')).pack(anchor='w')
            ttk.Label(op_frame, text=operacao['resultado'], wraplength=350).pack(anchor='w', padx=(10, 0))
            
            ttk.Separator(self.scrollable_frame, orient='horizontal').pack(fill=tk.X, padx=5, pady=5)

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))