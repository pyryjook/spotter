import configparser

def get_configs():
    '''TODO: Cache configs so that every function call does not init ConfigParser'''
    config = configparser.ConfigParser()
    config.read('configs.ini')

    if 'ApiKeys' not in config:
        raise ValueError('ApiKeys section not found from configs.ini')
    
    if 'Spotify' not in config:
        raise ValueError('Spotify section not found from configs.ini')
    
    keys = config['ApiKeys']
    spotify_settings = config['Spotify']
    
    return {
        'spotify_username': spotify_settings.get('UserName'),
        'client_id': keys.get('ClientId'),
        'client_secret': keys.get('ClientSecret'),
        'redirect_uri': keys.get('RedirectUri')
    }
