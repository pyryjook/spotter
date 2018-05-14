import urwid
import sys
from repository import scopes
from repository.auth import authorize_session
# Print debug to file that can be followed with $ tail
sys.stdout = open('stdout', 'w')
from pydux.create_store import create_store
from urwid_pydux import subscribe_urwid_redraw

from components.App import App
from reducers import spotter_app
from actions import get_main_menu

def open_app():
    store = create_store(spotter_app)
    store.dispatch(get_main_menu())
    root = App(store=store)
    loop = urwid.MainLoop(root)
    subscribe_urwid_redraw(store, loop)
    loop.run()

def get_scopes():
    return [getattr(scopes, prop) for  prop in dir(scopes) if "__" not in prop]

def authorize_user():
    scopes = get_scopes()
    authorize_session('pyryjook', " ".join(scopes))

def main():
    authorize_user()
    open_app()

if __name__ == '__main__':
    main()