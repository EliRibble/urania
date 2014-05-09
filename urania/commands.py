import os
import requests
import urania.connection

def get_devices(users=None):
    users = users if users is not None else urania.config.all_users()
    return [urania.connection.get_registered_devices(user) for user in users]

def download_track(user, track, path):
    url = urania.connection.get_stream_url(user, track['id'])
    response = requests.get(url)
    if not response.ok:
        raise Exception("Failed to get {}: {}".format(track['id'], response.text))
    with open(path, 'wb') as f:
        for block in response.iter_content(1024):
            if not block:
                break
            f.write(block)

def sync(users):
    for user in users:
        tracks = urania.connection.get_all_tracks(user)
        for track in tracks:
            path = "{}/{}.mp3".format(user.music_home, track['id'])
            if not os.path.exists(path):
                download_track(user, track, path)

from gmusicapi import Webclient, Mobileclient
import gmusicapi.exceptions
import getpass
import os
import pprint
import requests
import time
