from pydux.combine_reducers import combine_reducers

from .view import views
from .menu import menus

spotter_app = combine_reducers({
    'views': views,
    'menu': menus
})