from urwid import ExitMainLoop
from urwid_pydux import ConnectedComponent

from actions import show_top_songs, show_top_songs
from components.MainMenu import MainMenu as MainMenuComponent

class MainMenu(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {
            'menu': state['menu']
        }

    def choose_item(self, choose_view):
        if choose_view == 'top_songs':
            self.store['dispatch'](show_top_songs())   

    def exit_app(self):
        raise ExitMainLoop()

    def render_component(self, props):
        choices = props['menu']['items']
        print(choices)
        return MainMenuComponent(
            title = "Spotter",
            choices = choices,
            exit_app = self.exit_app,
            choose_item = self.choose_item
        )
