import tkinter as tk
from tkinter import ttk, messagebox

from src.services.movimentacao_service import movimentar_estoque
from src.database.estoque_repository import get_produto , listar_produtos


def criar_aba(frame, text_output):
    ttk.Label(frame, text="Código Produto (ID):").pack()
    entry_codigo = ttk.Entry(frame)
    entry_codigo.pack()

    ttk.Label(frame, text="Quantidade:").pack()
    entry_quant = ttk.Entry(frame)
    entry_quant.pack()

    ttk.Label(frame, text="Tipo de Movimentação:").pack()
    combo_tipo = ttk.Combobox(frame, values=["Entrada", "Saida"])
    combo_tipo.pack()

    ttk.Label(frame, text="Descrição (opcional):").pack()
    entry_desc = ttk.Entry(frame)
    entry_desc.pack()

    btn = ttk.Button(
        frame,
        text="Registrar Movimentação",
        command=lambda: executar(
            entry_codigo, entry_quant, combo_tipo, entry_desc, text_output
        ),
    )
    btn.pack(pady=10)

    btn = ttk.Button(
        frame,
        text="Verificar Estoque",
        command=lambda: total_estoque(text_output),
    )
    btn.pack(pady=10)


def executar(entry_codigo, entry_quant, combo_tipo, entry_desc, text_output):
    try:
        id_produto = int(entry_codigo.get())
        quantidade = int(entry_quant.get())
        tipo = combo_tipo.get()

        if not tipo:
            messagebox.showerror("Erro", "Selecione o tipo de movimentação!")
            return

        produto = get_produto(id_produto)
        if produto is None:
            messagebox.showerror("Erro", "Produto não encontrado!")
            return

        id_mov, erro = movimentar_estoque(id_produto, quantidade, tipo)

        if erro:
            messagebox.showerror("Erro", erro)
            return

        text_output.delete("1.0", "end")
        text_output.insert(
            "end",
            f"Movimentação registrada!\n"
            f"ID: {id_mov}\n"
            f"Produto: {produto['nome']}\n"
            f"Quantidade movida: {quantidade}\n"
            f"Tipo: {tipo}\n"
            f"Novo estoque: {get_produto(id_produto)['quantidade']}",
        )

    except ValueError:
        messagebox.showerror("Erro", "Preencha os campos corretamente!")


def total_estoque(text_output):
    text_output.delete("1.0", "end")

    produtos = listar_produtos()

    if not produtos:
        text_output.insert("end", "Estoque vazio!")
        return

    texto = "TOTAL DO ESTOQUE:\n\n"

    for p in produtos:
        texto += (
            f"ID (Código): {p['id']}\n"
            f"Produto: {p['nome']}\n"
            f"Quantidade: {p['quantidade']}\n"
            f"Preço: R$ {p['preco']:.2f}\n"
            + "-" * 50 + "\n"
        )

    text_output.insert("end", texto)
