from constants.actions import SHOW_TOP_SONGS
from constants.views import MAIN_MENU_VIEW, TOP_SONGS_VIEW
from pydux.extend import extend


def views(state=None, action=None):
    if action['type'] == SHOW_TOP_SONGS:
        return { 'view': TOP_SONGS_VIEW }
    else:
        return { 'view': MAIN_MENU_VIEW }