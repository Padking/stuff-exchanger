import shelve
from typing import Dict, List, Type

from aiogram import types

import config
import entities_worker


constants = config.Settings()


def get_users(filepath=constants.SHELVE_FILENAME, key='users') -> List:
    with shelve.open(filepath, flag='r') as users_storage:
        try:
            users = users_storage[key]
        except KeyError:  # Никто не пользовался ботом
            users = []

    return users


def update_users(users: List, msg: types.Message,
                 filepath=constants.SHELVE_FILENAME, key='users'):

    user_id = msg.from_user.id
    user = entities_worker.search_user(users, user_id)

    if users and user:
        return user

    users_fields_vals = (user_id, list(), list(), )
    new_user = entities_worker.create_entity(users_fields_vals)
    users.append(new_user)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users

    return new_user


def update_goods(users: List, user: Dict, msg: types.Message,
                 filepath=constants.SHELVE_FILENAME, key='users'):

    entities_worker.add_good(user, msg)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users


def update_assesments(users: List, c_query: types.CallbackQuery,
                      filepath=constants.SHELVE_FILENAME, key='users'):

    user, good_id = entities_worker.get_user_and_users_field(users,
                                                             c_query.message.photo[-1].file_unique_id)

    keys_assesements_vals = (c_query.from_user.id, good_id, c_query.data)
    assesment = entities_worker.create_entity(fields_names=constants.ASSESMENTS_OBJ_FIELDS,
                                              fields_vals=keys_assesements_vals)
    entities_worker.add_assesment(user, assesment)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users


def update_goods_name(users: List, msg: types.Message,
                      filepath=constants.SHELVE_FILENAME, key='users'):
    
    user = entities_worker.search_user(users, msg.from_user.id)

    try:
        entities_worker.change_goods_name(user, msg)
    # П-ль, который добавлял ранее вещи корректным способом,
    # пытается отправить название вещи (новой) раньше загрузки её фотографии
    except TypeError:
        pass
    else:
        with shelve.open(filepath, flag='w') as users_storage:
            users_storage[key] = users
