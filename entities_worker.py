import ast
import random
from typing import Dict, List, Tuple

from aiogram import types

import config


constants = config.Settings()


def add_good(user: Dict, msg: types.Message, goods='goods'):
    user[goods].append({
        'image': ast.literal_eval(str(msg.photo[-1])),
        'name': msg.caption  #FIXME
    })


def change_goods_name(user: Dict, msg: types.Message, goods='goods'):
    good = search_good(user[goods])
    good['name'] = msg.text


def add_assesment(user: Dict, assesment: Dict, assesments='assesments'):
    user[assesments].append(assesment)


def create_entity(fields_vals: Tuple,
                  fields_names=constants.USERS_OBJ_FIELDS) -> Dict:
    
    entity = dict(zip(fields_names, fields_vals))
    
    return entity


def get_random_good(users: List, user_id) -> Dict:
    """Получает любую вещь случайного П-ля.
    
    За исключением вещей П-ля, который отправил
    запрос боту

    """

    user = random.choice([user for user in users if user['user_id'] != user_id])
    good = random.choice(user['goods'])

    return good


def get_good(users: List, user_id):
    """Получает любую вещь конкретного П-ля."""

    user = search_user(users, user_id)
    good = random.choice(user['goods'])

    return good


def search_user(users: List, id_: int) -> Dict:
    for user in users:
        if user['user_id'] == id_:
            return user
    return {}


def search_good(goods: List, name=None) -> Dict:
    for good in goods:
        if good['name'] == name:
            return good


def get_user_and_users_field(users, by_file_unique_id):
    for user in users:
        for good_id, good in enumerate(user['goods'], 1):
            if good['image']['file_unique_id'] == by_file_unique_id:
                return user, good_id
