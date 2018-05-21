from constants.actions import UPDATE_LIST_CONTENT
from pydux.extend import extend
from .initial_state import INITIAL_STATE

def menus(state=INITIAL_STATE, action=None):
    if action['type'] == UPDATE_LIST_CONTENT:
        return extend(
            state,
            {
                'title': action['title'],
                'items': action['items'],
                'go_to_prev': action['go_to_prev']
            }
        )
    elif not state:
        return INITIAL_STATE
    else:
        return state