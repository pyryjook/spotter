from urwid import ExitMainLoop
from urwid_pydux import ConnectedComponent

from actions import show_top_songs
from components.MainMenu import MainMenu as MainMenuComponent


class MainMenu(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {
            'menu': state['menu']
        }

    def choose_item(self, choose_view):
        print(choose_view)

    def exit_app(self):
        raise ExitMainLoop()

    def render_component(self, props):
        choices = props['menu']['items']

        return MainMenuComponent(
            title = "Spotter",
            choices = choices,
            exit_app = self.exit_app,
            choose_item = self.choose_item
        )
