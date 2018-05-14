from pydux.combine_reducers import combine_reducers

from .menu import menus
from .player import player_state

spotter_app = combine_reducers({
    'menu': menus,
    'player': player_state
})