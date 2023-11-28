from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            artists.append(item)
        return artists

