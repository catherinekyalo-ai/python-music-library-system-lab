class Song:
    # Class attributes: shared by every Song, so they track the whole library
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    artist_count = {}  # the tests look for this name

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Each class method triggers whenever a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increment the total number of songs by one
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Only add genres we haven't seen, so the list stays unique
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Only add artists we haven't seen, so the list stays unique
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add the genre with 1 if new, otherwise increment it
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Add the artist with 1 if new, otherwise increment it
        cls.artists_count[artist] = cls.artists_count.get(artist, 0) + 1
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
