from gmusicapi import Webclient, Mobileclient
import logging

LOGGER = logging.getLogger('connection')
CLIENTS = {
        'webclient'     : {},
        'mobileclient'  : {},
}

def _get_client(clienttype, user):
    global CLIENTS
    try:
        return CLIENTS[clienttype][user]
    except KeyError:
        client = Webclient() if clienttype == 'webclient' else Mobileclient()
        LOGGER.debug("Logging in %s for %s", clienttype, user.name)
        success = client.login(user.username, user.password)
        if not success:
            raise Exception("Failed to log in as {} to webclient".format(user))
        CLIENTS[clienttype][user] = client
        return client

def get_registered_devices(user):
    webclient = _get_webclient('webclient', user)
    return webclient.get_registered_devices()

def get_stream_url(user, track_id):
    mobileclient = _get_client('mobileclient', user)
    url = mobileclient.get_stream_url(track_id, user.device_id)
    return url

def get_all_tracks(user):
    return _get_client('mobileclient', user).get_all_songs()
