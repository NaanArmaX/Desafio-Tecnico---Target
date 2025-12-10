from src.database.connection import get_connection

def reg_mov(id_mov,produto_id,tipo,quantidade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
    INSERT INTO movimentacoes (id,produto_id,tipo,quantidade) VALUES (?,?,?,?)
    """, (id_mov,produto_id,tipo,quantidade))
    conn.commit()
    conn.close()
