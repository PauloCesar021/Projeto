import sqlite3
conexao = sqlite3.connect('series.db')
cursor = conexao.cursor()
cursor.execute(
    """
        CREATE TABLE series(
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  
          nome TEXT NOT NULL,
          ano INTEGER NOT NULL,
          nota REAL NOT NULL,
          temporada INTEGER,
          duracao INTEGER,
          categoria TEXT
        );
    """
)
conexao.close()
print("a tabela de series foi criada com sucesso")