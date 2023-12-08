from media import Film, Series, Documentary, Clip
from actor import Actor

# Creating actors
actor1 = Actor("Actor 1")
actor2 = Actor("Actor 2")
actors_film = [actor1, actor2]

# Creating media instances
film1 = Film("Film 1", "Director 1", 8.5, "https://www.youtube.com/watch?v=123456", 120, actors_film, "Action")

# Showing information about the film
film1.showInfo()

# Downloading the film
film1.download()
