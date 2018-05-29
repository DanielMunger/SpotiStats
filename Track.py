class Track:
    """A Spotify Track."""
    def __init__(
    self, artist, title, duration, danceability, energy, key, loudness,
    acousticness, speechiness, instrumentalness, liveness, valence, mode
    ):
        self.artist = artist
        self.title = title
        self.duration = duration
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.acousticness = acousticness
        self.speechiness = speechiness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.mode = mode
