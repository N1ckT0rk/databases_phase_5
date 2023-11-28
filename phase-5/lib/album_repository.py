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

    # Find a single album by id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [
                                 album.title, album.release_year, album.artist_id])
        return None

    # Delete an artist by their id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [id])
        return None
