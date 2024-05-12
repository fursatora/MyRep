import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
