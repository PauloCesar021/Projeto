import sqlite3
conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()
id = (1,11)
cursor.execute(
    """
    DELETE FROM series
    WHERE id in (?,?)
    """,
    id 
)
conexao.commit()