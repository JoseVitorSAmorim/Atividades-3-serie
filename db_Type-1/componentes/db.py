import sqlite3
from datetime import date

def conectar_db():
    conn = sqlite3.connect('GreenQuest.db')
    cursor = conn.cursor()
    return conn, cursor

def criar_db():
    conn, cursor = conectar_db()
    
    #Cria a tabela se ela não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS atividades_sustentaveis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_acao TEXT,
        pontos INT,
        data_realizacao DATE
    );
    ''')
    conn.commit()
    conn.close()

def inserir_atividade(descricao_acao, pontos):
    conn, cursor = conectar_db()
    cursor.execute('''
        INSERT INTO atividades_sustentaveis (descricao_acao, pontos, data_realizacao) VALUES (?, ?, ?)
    ''', (descricao_acao, pontos, date.today()))
    conn.commit()
    conn.close()

def listar_atividades():
    conn, cursor = conectar_db()
    cursor.execute('SELECT * FROM atividades_sustentaveis')
    atividades = cursor.fetchall()
    conn.close()
    return atividades