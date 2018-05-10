from urwid import ExitMainLoop
from urwid_pydux import ConnectedComponent

from actions import show_top_songs
from components.MainMenu import MainMenu as MainMenuComponent

choices = u'Chapman Cleese Gilliam Idle Jones Palin'.split()

class MainMenu(ConnectedComponent):
    def menu(self, title, choices):
        return 1

    def choose_item(self, button, choice):
        return 1

    def exit_app(self, button):
        return ExitMainLoop()

    def render_component(self, props):
        choices = [
            "boo",
            "hoo",
            "exit"
        ]

        return MainMenuComponent(
            title = "Spotter",
            choices = choices,
            exit_app = self.exit_app
        )
