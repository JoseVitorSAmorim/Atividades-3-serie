import sqlite3

# 1. Conecta ao banco de dados (ou cria se não existir)
def conectar_db(){
conn = sqlite3.connect('GreenQuest.db')
cursor = conn.cursor()
}

# 2. Criando a tabela (DDL)
def criar_db(){
cursor.execute('''
    CREATE TABLE atividades_sustentaveis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_acao TEXT,
        pontos INT,
        data_realizacao DATE
    )
''')
}

# 3. Inserindo dados (DML)
def insert(){
cursor.execute("INSERT INTO atividades_sustentaveis (descricao_acao, pontos) VALUES ()")
conn.commit()
}

# 4. Consultando dados (DQL)
def select(){
cursor.execute("SELECT * FROM ")
print(cursor.fetchall())
}