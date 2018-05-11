import urwid
import sys
# Print debug to file that can be followed with $ tail
sys.stdout = open('stdout', 'w')
from pydux.create_store import create_store
from urwid_pydux import subscribe_urwid_redraw

from components.App import App
from reducers import spotter_app
from actions import render_main_menu

def main():
    store = create_store(spotter_app)
    store.dispatch(render_main_menu())
    root = App(store=store)
    loop = urwid.MainLoop(root)
    subscribe_urwid_redraw(store, loop)
    loop.run()

if __name__ == '__main__':
    main()