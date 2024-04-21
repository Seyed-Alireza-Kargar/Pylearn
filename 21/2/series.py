from media import Media

class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, num_episodes):
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.num_episodes = num_episodes
