# Importação do SQLite

import sqlite3 as lite

# Criando banco de dados

con=lite.connect("lista.db")

def inserir(i):
    with con:
        cur = con.cursor()
        query= "INSERT INTO tarefa(nome) VALUES('?') "
        cur.execute(query, i)

def selecionar(): 
    lista_tarefa=[]
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa ")
        row=cur.fetchall()
        for r in row:
             lista_tarefa.append(r)
    
# with con:
#     cur = con.cursor()
#     cur.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")