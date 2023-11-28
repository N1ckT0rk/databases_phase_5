from lib.album_repository import *
from lib.album import *

# When we use the find method we find an instance of object
# with the id
def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    
    album = repository.find(1)
    assert album == Album(1, "Doolittle", 1989, 1)

