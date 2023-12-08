from pytube import YouTube

class Media:
    def __init__(self, name, director, imdb_score, url, duration, casts):
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    def showInfo(self):
        print(f"Name: {self.name}")
        print(f"Director: {self.director}")
        print(f"IMDB Score: {self.imdb_score}")
        print(f"URL: {self.url}")
        print(f"Duration: {self.duration}")
        print("Casts:")
        for actor in self.casts:
            print(f"- {actor.name}")

    def download(self):
        yt = YouTube(self.url)
        yt.streams.first().download()


class Film(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, genre):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre


class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, num_episodes):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.num_episodes = num_episodes


class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, topic):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.topic = topic


class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, purpose):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.purpose = purpose
