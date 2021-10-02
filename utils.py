import ast
import random
import shelve
from typing import Dict, List, Tuple

from aiogram import types

import config


constants = config.Settings()


def add_good(user: Dict, msg: types.Message, goods='goods'):
    user[goods].append({
        'image': ast.literal_eval(str(msg.photo[-1])),
        'name': msg.caption  #FIXME
    })


def add_assesment(user: Dict, assesment: Dict, assesments='assesments'):
    user[assesments].append(assesment)


def create_entity(fields_vals: Tuple,
                  fields_names=constants.USERS_OBJ_FIELDS) -> Dict:
    
    entity = dict(zip(fields_names, fields_vals))
    
    return entity


def get_good(users, user_id) -> Dict:
    """Получает любую вещь случайного П-ля.
    
    За исключением вещей П-ля, который отправил
    запрос боту

    """

    user = random.choice([user for user in users if user['user_id'] != user_id])
    good = random.choice(user['goods'])

    return good


def search_user(users: List, id_: int) -> Dict:
    for user in users:
        if user['user_id'] == id_:
            return user
    return {}


def get_user_and_users_field(users, by_file_unique_id):

    for user in users:
        for good_id, good in enumerate(user['goods'], 1):
            if good['image']['file_unique_id'] == by_file_unique_id:
                return user, good_id


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
    user = search_user(users, user_id)

    if users and user:
        return user

    users_fields_vals = (user_id, list(), list(), )
    new_user = create_entity(users_fields_vals)
    users.append(new_user)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users

    return new_user


def update_goods(users: List, user: Dict, msg: types.Message,
                 filepath=constants.SHELVE_FILENAME, key='users'):

    add_good(user, msg)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users


def update_assesments(users: List, c_query: types.CallbackQuery,
                      filepath=constants.SHELVE_FILENAME, key='users'):

    user, good_id = get_user_and_users_field(users, c_query.message.photo[-1].file_unique_id)

    keys_assesements_vals = (c_query.from_user.id, good_id, c_query.data)
    assesment = create_entity(fields_names=constants.ASSESMENTS_OBJ_FIELDS, fields_vals=keys_assesements_vals)
    add_assesment(user, assesment)

    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users
