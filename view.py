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


## funcoes delete
def deletar_categoria(id):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM categoria WHERE id = ?"
        cur.execute(query, (id,))
def deletar_Receitas(id):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query, (id,))
        

def deletar_gasto(id):
    with conn:
        cur = conn.cursor()
        query = "DELETE FROM Gastos WHERE id = ?"
        cur.execute(query, (id,))
       

## ver dados
def ver_categorias():

    lista_itens = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM categorias"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens

## ver dados
def ver_categorias():

    lista_itens = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM receitas"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens

## ver dados
def ver_categorias():

    lista_itens = []
    with conn:
        cur = conn.cursor()
        query = "SELECT * FROM Gastos"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens
