import sqlite3

conn = sqlite3.connect('biblioteca_jogos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    genero TEXT NOT NULL,
    preco REAL NOT NULL,
    plataforma TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("Banco de dados e tabela criados com sucesso!")