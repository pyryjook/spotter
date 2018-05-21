from constants.actions import GET_CURRENT_PLAYING_SONG
from pydux.extend import extend
from .initial_state import INITIAL_STATE

def player_state(state=INITIAL_STATE, action=None):
    if action['type'] == GET_CURRENT_PLAYING_SONG:
        return extend(state, {
            'current_song': action['current_song']
        })
    elif not state:
        return INITIAL_STATE
    else:
        return state
