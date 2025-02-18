import pytest
from lib.song import Song  # Adjust the import path based on your directory structure

def setup_function():
    # Reset class attributes before each test
    Song.count = 0
    Song.genres = []
    Song.artists = []
    Song.genre_count = {}
    Song.artist_count = {}

def test_song_initialization():
    ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
    assert ninety_nine_problems.name == "99 Problems"
    assert ninety_nine_problems.artist == "Jay-Z"
    assert ninety_nine_problems.genre == "Rap"

def test_song_count():
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Billie Jean", "Michael Jackson", "Pop")
    assert Song.count == 2

def test_unique_genres():
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Billie Jean", "Michael Jackson", "Pop")
    Song("Another Brick in the Wall", "Pink Floyd", "Rock")
    Song("Hey Jude", "The Beatles", "Rock")
    assert set(Song.genres) == {"Rap", "Pop", "Rock"}

def test_unique_artists():
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Billie Jean", "Michael Jackson", "Pop")
    Song("Another Brick in the Wall", "Pink Floyd", "Rock")
    Song("Hey Jude", "The Beatles", "Rock")
    assert set(Song.artists) == {"Jay-Z", "Michael Jackson", "Pink Floyd", "The Beatles"}

def test_genre_count():
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Billie Jean", "Michael Jackson", "Pop")
    Song("Another Brick in the Wall", "Pink Floyd", "Rock")
    Song("Hey Jude", "The Beatles", "Rock")
    assert Song.genre_count == {"Rap": 1, "Pop": 1, "Rock": 2}

def test_artist_count():
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Billie Jean", "Michael Jackson", "Pop")
    Song("Another Brick in the Wall", "Pink Floyd", "Rock")
    Song("Hey Jude", "The Beatles", "Rock")
    assert Song.artist_count == {"Jay-Z": 1, "Michael Jackson": 1, "Pink Floyd": 1, "The Beatles": 1}