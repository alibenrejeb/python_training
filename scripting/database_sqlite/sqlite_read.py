import sqlite3

connection = sqlite3.connect("albums.db")
cursor = connection.cursor()

# cursor.execute("SELECT * FROM artist")
# artists = cursor.fetchall()
# print(artists)

# cursor.execute("SELECT * FROM album WHERE year_released > 1996")
# albums = cursor.fetchall()
# print(albums)

cursor.execute("SELECT title FROM album a INNER JOIN artist b ON a.artist_id = b.artist_id WHERE b.name = 'Celine Dion'")
albums = cursor.fetchall()
print(albums)

connection.close()
