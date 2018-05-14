from urwid import ExitMainLoop
from urwid_pydux import ConnectedComponent

from actions import get_top_songs, get_main_menu, get_current_song
from components.Menu import Menu as MenuComponent
from repository.player import play_song

class Menu(ConnectedComponent):
    def map_state_to_props(self, state, own_props):
        return {
            'menu': state['menu'],
            'player': state['player']
        }

    def choose_item(self, choose_view):
        if choose_view == 'top_songs':
            self.store['dispatch'](get_top_songs())
        elif choose_view == 'main_menu':
            self.store['dispatch'](get_main_menu())
        else:
            play_song(choose_view)
            self.store['dispatch'](get_current_song())
        

    def exit_app(self):
        raise ExitMainLoop()

    def render_component(self, props):
        choices = props['menu']['items']
        return MenuComponent(
            title = "Spotter",
            choices = choices,
            exit_app = self.exit_app,
            choose_item = self.choose_item,
            go_to_prev = props['menu']['go_to_prev'],
            current_song = props['player']['current_song']
        )
