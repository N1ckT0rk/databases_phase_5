from lib.album import Album

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        artists = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            artists.append(item)
        return artists

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [id])
        for row in rows:
            return Album(row["id"], row["title"], row["release_year"], row["artist_id"])