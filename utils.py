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
        'name': msg.caption
    })


def create_user(fields_vals: Tuple,
                fields_names=constants.USERS_OBJ_FIELDS) -> Dict:
    
    user = dict(zip(fields_names, fields_vals))
    
    return user


def get_good(user_id) -> Dict:
    """Получает любую вещь случайного П-ля.
    
    За исключением вещей П-ля, который отправил
    запрос боту

    """
    
    users = get_users()
    user = random.choice([user for user in users if user['user_id'] != user_id])
    good = random.choice(user['goods'])

    return good


def search_user(users: List, id_: int) -> Dict:
    for user in users:
        if user['user_id'] == id_:
            return user
    else:
        error_msg = (
            f'Пользователь с {id_} не найден!'
        )
        raise ValueError(error_msg)


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

    try:
        user = search_user(users, user_id)
    except ValueError:  # К боту обратился новый П-ль
        users_fields_vals = (user_id, list(), )
        user = create_user(users_fields_vals)
        add_good(user, msg)
        users.append(user)
    else:  # Добавление очередной вещи П-я
        add_good(user, msg)
        
    with shelve.open(filepath, flag='w') as users_storage:
        users_storage[key] = users
