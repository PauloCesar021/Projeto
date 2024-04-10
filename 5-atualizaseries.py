import sqlite3
conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()
id = 1
cursor.execute(
    """
    UPDATE series set nome = ?
    WHERE id = ?
    """,
    ("Sobrenatural", 4)
    
)
conexao.commit()