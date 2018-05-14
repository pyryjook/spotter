from constants.actions import SHOW_MAIN_MENU, SHOW_TOP_SONGS, UPDATE_LIST_CONTENT
from repository import get_top_songs as get_top_songs_from_api

def _map_songs(songs):
    ''' maps songs tuple to string in format: 1. artist1, artist2 - song name. First item in tuple is song index (zero based)'''
    return [ (str(song[0] + 1)+". "+", ".join(song[1]['artists'])+" - "+song[1]['name'], song[1]['song_spotify_uri']) for song in songs]

def show_main_menu():
    return { 'type': SHOW_MAIN_MENU }

def show_top_songs():
    return { 'type': SHOW_MAIN_MENU }

def get_main_menu():
    return {
        'type': UPDATE_LIST_CONTENT,
        'title': None,
        'items': [
            ('Most listened songs', 'top_songs'),
            ('Exit Spotter... Bye!', 'exit')
        ]
    }

def get_top_songs():
    mapped_songs = _map_songs(get_top_songs_from_api('pyryjook'))

    return {
        'type': UPDATE_LIST_CONTENT,
        'title': None,
        'items': mapped_songs
    }

