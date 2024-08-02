import sqlite3
from BirdCipher import username, nickname, hash1

miConexion = sqlite3.connect("Players")


miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE Players (name_player varchar(50), nickname varchar(50), password varchar(256))")

miCursor.execute("INSERT INTO players VALUES()")










miConexion.close()