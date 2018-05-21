import sys
import spotipy
import spotipy.util as util
from misc import get_configs

session = ''

def get_session():
    global session

    return session


def authorize_session(username, scope):
    global session
    configs = get_configs()
    client_id = configs.get('client_id')
    client_secret = configs.get('client_secret')
    redirect_uri = configs.get('redirect_uri')
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    session = spotipy.Spotify(auth=token)

    return session
