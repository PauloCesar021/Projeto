import sqlite3
conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()
dados = cursor.execute(
    "SELECT * FROM series"
)
print(dados.fetchall())