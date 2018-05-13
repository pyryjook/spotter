from functools import reduce
import operator
from .auth import get_session

def get_songs_data(username):
    sp = get_session(username)
    return sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')

def get_top_songs(username):
    songs_data = get_songs_data(username)

    songs = [{
        'artists': [artist.get('name') for artist in song.get('artists')],
        'name': song.get('name'),
        'song_spotify_uri': song.get('uri')
    } for song in songs_data['items']]

    return list(enumerate(songs))