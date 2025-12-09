from tkcalendar import DateEntry
from tkinter import ttk
import tkinter as tk
from tkinter import ttk, messagebox
from src.services.juros import calcular_juros


def criar_aba(frame, text_output):
    ttk.Label(frame, text="Valor:").pack()
    entry_valor = ttk.Entry(frame)
    entry_valor.pack()

    ttk.Label(frame, text="Vencimento:").pack()
    entry_data = DateEntry(frame, date_pattern="dd/mm/yyyy")
    entry_data.pack()

    btn = ttk.Button(
        frame,
        text="Calcular Juros",
        command=lambda: executar(entry_valor, entry_data, text_output),
    )
    btn.pack(pady=10)


def executar(entry_valor, entry_data, text_output):
    try:
        valor = float(entry_valor.get())
        venc = entry_data.get()

        dias, juros, total = calcular_juros(valor, venc)

        if dias is None:
            messagebox.showerror("Erro", total)
            return

        text_output.delete("1.0", "end")
        text_output.insert(
            "end",
            f"Dias de atraso: {dias}\n"
            f"Juros: R${juros:.2f}\n"
            f"Total a pagar: R${total:.2f}",
        )
    except:
        messagebox.showerror("Erro", "Valor inválido!")
