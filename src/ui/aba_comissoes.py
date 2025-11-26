from tkinter import ttk
from data.vendas import vendas
from services.comissoes import calc_comi


def criar_aba(frame,text_output):
    btn = ttk.Button(frame, text="Calcular Comissões",
                     command=lambda: mostrar(text_output))
    btn.pack(pady=10)


def mostrar(text_output):
    resultado = calc_comi(vendas)
    texto = ""

    for vendedor, valor in resultado.items():
        texto += f"{vendedor}: R$ {valor:.2f}\n"

    text_output.delete("1.0","end")
    text_output.insert("end",texto)