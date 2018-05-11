from constants.actions import UPDATE_LIST_CONTENT
from constants.views import MAIN_MENU_VIEW, TOP_SONGS_VIEW
from pydux.extend import extend

def menus(state=None, action=None):
    print(action, UPDATE_LIST_CONTENT)
    if action['type'] == UPDATE_LIST_CONTENT:
        print('oh yes')
        return {
            'title': action['title'],
            'items': action['items']
        }
    else:
        return {
            'title': None,
            'items': []
        }