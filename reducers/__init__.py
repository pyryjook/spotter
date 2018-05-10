from pydux.combine_reducers import combine_reducers

from .view import views

spotter_app = combine_reducers({
    'views': views
})