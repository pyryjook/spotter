from constants.actions import UPDATE_LIST_CONTENT
from pydux.extend import extend

def menus(state=None, action=None):
    if action['type'] == UPDATE_LIST_CONTENT:
        return {
            'title': action['title'],
            'items': action['items'],
            'go_to_prev': action['go_to_prev']
        }
    else:
        return {
            'title': None,
            'items': [],
            'go_to_prev': ('', '')
        }