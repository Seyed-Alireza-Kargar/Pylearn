from actor import Actor
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

# Creating actors
actor1 = Actor("Actor 1")
actor2 = Actor("Actor 2")
actors_film = [actor1, actor2]

# Creating media instances
film1 = Film("Film 1", "Director 1", 8.5, "https://www.youtube.com/watch?v=123456", 120, actors_film, "Action")
series1 = Series("Series 1", "Director 2", 9.0, "https://www.youtube.com/watch?v=789012", 45, [actor1], 10)
doc1 = Documentary("Documentary 1", "Director 3", 7.8, "https://www.youtube.com/watch?v=345678", 60, [actor2], "Nature")
clip1 = Clip("Clip 1", "Director 4", 6.5, "https://www.youtube.com/watch?v=901234", 5, [actor1, actor2], "Tutorial")

# Showing information about the media
film1.showInfo()
series1.showInfo()
doc1.showInfo()
clip1.showInfo()

# Downloading media
film1.download()
series1.download()
doc1.download()
clip1.download()
