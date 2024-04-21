import sqlite3
from actor import Actor
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

# Connection to SQLite database
conn = sqlite3.connect('media.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS media
             (name text, director text, imdb_score real, url text, duration integer, type text, genre_or_topic text, num_episodes integer, purpose text)''')

# Insert a row of data into the table
def insert_media(media):
    if isinstance(media, Film):
        c.execute("INSERT INTO media VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)", (media.name, media.director, media.imdb_score, media.url, media.duration, 'Film', media.genre))
    elif isinstance(media, Series):
        c.execute("INSERT INTO media VALUES (?, ?, ?, ?, ?, ?, NULL, ?, NULL)", (media.name, media.director, media.imdb_score, media.url, media.duration, 'Series', media.num_episodes))
    elif isinstance(media, Documentary):
        c.execute("INSERT INTO media VALUES (?, ?, ?, ?, ?, ?, ?, NULL, NULL)", (media.name, media.director, media.imdb_score, media.url, media.duration, 'Documentary', media.topic))
    elif isinstance(media, Clip):
        c.execute("INSERT INTO media VALUES (?, ?, ?, ?, ?, ?, NULL, NULL, ?)", (media.name, media.director, media.imdb_score, media.url, media.duration, 'Clip', media.purpose))
    else:
        print("Unsupported media type")

# Commit changes and close connection
conn.commit()

# Creating actors
actor1 = Actor("Actor 1")
actor2 = Actor("Actor 2")
actors_film = [actor1, actor2]

# Creating media instances
film1 = Film("Film 1", "Director 1", 8.5, "https://www.youtube.com/watch?v=123456", 120, actors_film, "Action")
series1 = Series("Series 1", "Director 2", 9.0, "https://www.youtube.com/watch?v=789012", 45, [actor1], 10)
doc1 = Documentary("Documentary 1", "Director 3", 7.8, "https://www.youtube.com/watch?v=345678", 60, [actor2], "Nature")
clip1 = Clip("Clip 1", "Director 4", 6.5, "https://www.youtube.com/watch?v=901234", 5, [actor1, actor2], "Tutorial")

# Insert media into database
insert_media(film1)
insert_media(series1)
insert_media(doc1)
insert_media(clip1)

# Query and display all media
c.execute("SELECT * FROM media")
rows = c.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()
