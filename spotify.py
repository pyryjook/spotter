import urwid
import sys
from repository import scopes
from repository.auth import authorize_session
# Print debug to file that can be followed with $ tail
# sys.stdout = open('stdout', 'w')
from pydux.create_store import create_store
from urwid_pydux import subscribe_urwid_redraw

from actions import get_main_menu, get_current_song
from misc import get_configs
from components.App import App
from reducers import spotter_app

def open_app():
    store = create_store(spotter_app)
    store.dispatch(get_current_song())
    store.dispatch(get_main_menu())
    root = App(store=store)
    loop = urwid.MainLoop(root)
    subscribe_urwid_redraw(store, loop)
    loop.run()

def get_scopes():
    return [getattr(scopes, prop) for  prop in dir(scopes) if "__" not in prop]

def authorize_user(username):
    scopes = get_scopes()

    authorize_session(username, " ".join(scopes))

def main():
    config = get_configs()
    authorize_user(config.get('spotify_username'))
    open_app()

if __name__ == '__main__':
    main()