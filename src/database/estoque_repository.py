import sqlite3
from .connection import get_connection


def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, quantidade, preco FROM estoque")
    rows = cursor.fetchall()
    conn.close()

    produtos = []
    for r in rows:
        produtos.append({
            "id": r[0],
            "nome": r[1],
            "quantidade": r[2],
            "preco": r[3]
        })

    return produtos


def get_produto(id_produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, nome, quantidade, preco FROM estoque WHERE id = ?",
        (id_produto,)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "nome": row[1],
        "quantidade": row[2],
        "preco": row[3]
    }


def att_produtos(id_produto, nome, quantidade, preco):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE estoque SET nome = ?, quantidade = ?, preco = ? WHERE id = ?",
        (nome, quantidade, preco, id_produto)
    )

    conn.commit()
    conn.close()

def del_produtos(id_produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM estoque WHERE id = ?", (id_produto,))
    conn.commit()
    conn.close()
