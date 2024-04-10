import sqlite3
conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()
cursor.execute(
    """
        INSERT INTO series(nome, ano, nota, temporada, duracao, categoria)
        VALUES ('Sherlock Holmes', 2010, 7.0 , 4 , 60 , 'mistério')
    """
)
conexao.commit()
conexao.close()