import tkinter as tk
from tkinter import ttk

from ui import aba_comissoes, aba_estoque, aba_juros

def open_window():
    root = tk.Tk()
    root.title("Sistema – Vendas, Estoque e Juros")
    root.geometry("650x600")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    text_output = tk.Text(root, height=10, font=("Arial", 12))
    text_output.pack(fill="both")

    # abas:
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)

    notebook.add(frame1, text="Comissões")
    notebook.add(frame2, text="Estoque")
    notebook.add(frame3, text="Juros")

    aba_comissoes.criar_aba(frame1, text_output)
    #aba_estoque.criar_aba(frame2, text_output)
    #aba_juros.criar_aba(frame3, text_output)

    root.mainloop()
