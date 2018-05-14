from pydux.combine_reducers import combine_reducers

from .menu import menus

spotter_app = combine_reducers({
    'menu': menus
})