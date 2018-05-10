from urwid import Divider, Overlay, Frame, Filler, SolidFill, CENTER, RELATIVE, MIDDLE
from urwid_pydux import ConnectedComponent

from urwid import Text, Button
from urwid_pydux import Component

from containers.MainMenu import MainMenu


class App(ConnectedComponent):
    def render_component(self, props):
        print(props)
        return Overlay(
            top_w=MainMenu(store=props['store']),
            bottom_w=SolidFill(u'\N{DARK SHADE}'),
            align=CENTER,
            width=(RELATIVE, 95),
            valign=MIDDLE,
            height=(RELATIVE, 95),
            min_width=20,
            min_height=20,
        )