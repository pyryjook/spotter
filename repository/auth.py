import sys
import spotipy
import spotipy.util as util
from misc import get_configs

sessions = {}

SCOPE = "user-top-read"

def get_session(username):
    global sessions

    if SCOPE not in sessions:
        configs = get_configs()
        client_id = configs.get('client_id')
        client_secret = configs.get('client_secret')
        redirect_uri = configs.get('redirect_uri')
        token = util.prompt_for_user_token(username, SCOPE, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
        sessions[SCOPE] = spotipy.Spotify(auth=token)

    return sessions[SCOPE]
