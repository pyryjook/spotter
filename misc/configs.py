import configparser

def get_configs():
    config = configparser.ConfigParser()
    config.read('configs.ini')

    if 'ApiKeys' not in config:
        raise ValueError('ApiKeys section not found from configs.ini')
    
    keys = config['ApiKeys']
    
    return {
        'client_id': keys.get('ClientId'),
        'client_secret': keys.get('ClientSecret'),
        'redirect_uri': keys.get('RedirectUri')
    }
