import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('Usuarios.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    Id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Login TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")

print("Conectado ao Banco ")
