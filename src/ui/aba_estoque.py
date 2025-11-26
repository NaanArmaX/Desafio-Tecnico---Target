import tkinter as tk
from tkinter import ttk, messagebox

from data.estoque import estoque
from services.estoque_service import movimentar_estoque

def criar_aba(frame, text_output):
    ttk.Label(frame, text="Código Produto:").pack()
    entry_codigo = ttk.Entry(frame); entry_codigo.pack()

    ttk.Label(frame, text="Quantidade:").pack()
    entry_quant = ttk.Entry(frame); entry_quant.pack()

    ttk.Label(frame, text="Tipo:").pack()
    combo_tipo = ttk.Combobox(frame, values=["Entrada", "Saída"])
    combo_tipo.pack()

    ttk.Label(frame, text="Descrição (opcional):").pack()
    entry_desc = ttk.Entry(frame); entry_desc.pack()

    btn = ttk.Button(
        frame,
        text="Registrar Movimentação",
        command=lambda: executar(entry_codigo, entry_quant, combo_tipo, entry_desc, text_output)
    )
    btn.pack(pady=10)

    btn = ttk.Button(
        frame,
        text="Verificar Estoque",
        command=lambda: total_estoque(text_output)
    )
    btn.pack(pady=10)

def executar(entry_codigo, entry_quant, combo_tipo, entry_desc, text_output):
    try:
        codigo = int(entry_codigo.get())
        quantidade = int(entry_quant.get())
        tipo = combo_tipo.get()

        item = next((p for p in estoque if p["codigo"] == codigo), None)

        if item is None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        id_mov, erro = movimentar_estoque(item, quantidade, tipo)

        if erro:
            messagebox.showerror("Erro", erro)
            return

        text_output.delete("1.0", "end")
        text_output.insert("end",
            f"Movimentação registrada!\n"
            f"ID: {id_mov}\n"
            f"Produto: {item['descricao']}\n"
            f"Estoque final: {item['estoque']}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos corretamente!")


def total_estoque(text_output):
    text_output.delete("1.0", "end")

    if not estoque:
        text_output.insert("end", "Estoque vazio!")
        return

    texto = "TOTAL DO ESTOQUE:\n\n"

    for item in estoque:
        texto += (
            f"Código: {item['codigo']}\n"
            f"Produto: {item['descricao']}\n"
            f"Quantidade: {item['estoque']}\n"
            "-------------------------\n"
        )

    text_output.insert("end", texto)
