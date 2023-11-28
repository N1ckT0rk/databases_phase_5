from lib.album import Album

"""
Album constructs with an id, title, release year, and artist id
"""
def test_albums_constructs():
    album = Album(1, "Test Title", 1997, 3)
    assert album.id == 1
    assert album.release_year == 1997
    assert album.artist_id == 3

"""
Format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 1997, 3)
    assert str(album) == "Album(1, Test Title, 1997, 3)"


"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 =  Album(1, "Test Title", 1997, 3)
    album2 =  Album(1, "Test Title", 1997, 3)
    assert album1 == album2

