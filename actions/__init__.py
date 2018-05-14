from constants.actions import UPDATE_LIST_CONTENT, GET_CURRENT_PLAYING_SONG
from repository import get_top_songs as get_top_songs_from_api, get_current_song as get_current_song_from_api

def get_main_menu():
    return {
        'type': UPDATE_LIST_CONTENT,
        'title': None,
        'go_to_prev': ('Exit Spotter... Bye!', 'exit'),
        'items': [
            ('Most listened songs', 'top_songs')
        ]
    }

def get_top_songs():
    def _map_songs(songs):
        ''' Maps songs tuple to string in format: 1. artist1, artist2 - song name. First item in tuple is song index (zero based)'''
        return [ (str(song[0] + 1)+". "+", ".join(song[1]['artists'])+" - "+song[1]['name'], song[1]['song_spotify_uri']) for song in songs]
    
    mapped_songs = _map_songs(get_top_songs_from_api('pyryjook'))

    return {
        'type': UPDATE_LIST_CONTENT,
        'title': None,
        'go_to_prev': ('Back to Main Menu', 'main_menu'),
        'items': mapped_songs
    }

def get_current_song():
    def map_song_name(song):
        return ", ".join(song.get('artists')) + " - " + song.get('name')

    return {
        'type': GET_CURRENT_PLAYING_SONG,
        'current_song': map_song_name(get_current_song_from_api())
    }

