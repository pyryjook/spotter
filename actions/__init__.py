from constants.actions import SHOW_MAIN_MENU, SHOW_TOP_SONGS, UPDATE_LIST_CONTENT

def show_main_menu():
    return { 'type': SHOW_MAIN_MENU }

def show_top_songs():
    return { 'type': SHOW_MAIN_MENU }

def render_main_menu():
    return {
        'type': UPDATE_LIST_CONTENT,
        'title': None,
        'items': [
            ('Most listened songs', 'top_songs'),
            ('Exit Spotter ->', 'exit')
        ]
    }