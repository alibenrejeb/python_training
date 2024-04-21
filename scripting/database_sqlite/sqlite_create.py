import sqlite3

connection = sqlite3.connect("albums.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE artist (
    artist_id INTEGER NOT NULL PRIMARY KEY, 
    name VARCHAR);""")

cursor.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artist_id INTEGER REFERENCES artiste,
    title VARCHAR,
    year_released INTEGER);""")

cursor.execute('INSERT INTO artist (name) VALUES ("Michael Jackson");')
artist_id_1 = cursor.lastrowid
cursor.execute('INSERT INTO artist (name) VALUES ("Celine Dion");')
artist_id_2 = cursor.lastrowid

cursor.execute('INSERT INTO album (artist_id, title, year_released) VALUES (' + str(artist_id_1) + ', "Thriller", 1982);')
cursor.execute('INSERT INTO album (artist_id, title, year_released) VALUES (' + str(artist_id_2) + ', "Falling into You", 1996);')
cursor.execute('INSERT INTO album (artist_id, title, year_released) VALUES (' + str(artist_id_2) + ', "Let\'s Talk About Love", 1997);')

connection.commit()
connection.close()
