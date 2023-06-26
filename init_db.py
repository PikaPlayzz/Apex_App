import sqlite3

connection = sqlite3.connect('player.db')


with open('schema.sql', "r") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()