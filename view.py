import sqlite3 as lite

# criando conexão com o banco de dados
conn = lite.connect('dados.db')

#inserir categorias
def inserir_categoria(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO categorias (categoria) VALUES (?)"
        cur.execute(query, (i,))

#inserir receutas
def inserir_categoria(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))


#inserir gastos
def inserir_categoria(i):
    with conn:
        cur = conn.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, (i,))