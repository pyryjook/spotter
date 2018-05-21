from .auth import get_session

def play_song(spotify_uri):
    sp = get_session()
    return sp.start_playback(uris = [spotify_uri])

def get_song_info(id):
    sp = get_session()
    return sp.track(track_id = id)

def get_current_song():
    sp = get_session()
    current_track = sp.current_playback()

    song = None

    if current_track:
        song = get_song_info(current_track['item']['id'])

        song = {
            'artists': [artist.get('name') for artist in song.get('artists')],
            'name': song.get('name'),
            'song_spotify_uri': song.get('uri')
        }
    else:
        song = {
            'artists': ['Choose a song'],
            'name': 'and chill',
            'song_spotify_uri': None
        }
    return song