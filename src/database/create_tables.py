from .connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL
        )
            """)
    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacoes (
        id TEXT PRIMARY KEY,
        produto_id INTEGER NOT NULL,
        tipo TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (produto_id) REFERENCES estoque(id)
    )
            """)
    
    conn.commit()
    conn.close


if __name__ == "__main__":
    create_table()
