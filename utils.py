import json


def get_users(filepath):
    with open(filepath, encoding='utf-8') as users_storage:
        users = json.load(users_storage)['users']

    return users


def update_users(users, filepath):
    with open(filepath, 'w', encoding='utf-8') as users_storage:
        json.dump(users, users_storage)
