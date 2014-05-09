import json
import collections

class User(object):
    def __init__(self, name, username, password, device_id, music_home):
        self.name = name
        self.username = username
        self.password = password
        self.device_id = device_id
        self.music_home = music_home

    def __repr__(self):
        return 'User {}'.format(self.name)

def load(configpath):
    with open(configpath, 'r') as f:
        content = f.read()

    load.config = json.loads(content)
    load.users = []
    for user, values in load.config['users'].items():
        load.users.append(User(user, values['username'], values['password'], values['device_id'], values['music_home']))

def all_users():
    return load.users

def get_user(name):
    for user in load.users:
        if user.name == name:
            return user
    raise Exception("Cannot find configured user with the name '{}".format(name))
