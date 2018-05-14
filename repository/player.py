from .auth import get_session

def play_song(spotify_uri):
    sp = get_session()
    return sp.start_playback(uris = [spotify_uri])