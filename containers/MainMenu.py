from urwid import Filler, Text
from urwid_pydux import ConnectedComponent

from actions import show_top_songs

class MainMenu(ConnectedComponent):
    def render_component(self, props):
        txt = Text(u"Hello World")

        return Filler(txt, 'top')