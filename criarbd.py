import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('dados.db')


#criando tabela de categorias
with conn:
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')

 #criando tabela de receitas
with conn:
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Receitas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria text, adicionado_em Date, valor decimal
        )
    ''')

#criando tabela de gastos
with conn:
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria text, retirado_em Date, valor decimal
        )
    ''')