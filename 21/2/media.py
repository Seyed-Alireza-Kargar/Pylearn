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
