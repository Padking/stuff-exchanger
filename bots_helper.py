from typing import Dict, List, Tuple

from aiogram import types

from config import buttons_labels_callback_data
from entities_worker import get_user_and_users_field


def get_keyboard(buttons_labels_callback_data: Dict=buttons_labels_callback_data, buttons=None):

    buttons = buttons or []
    keyboard = types.InlineKeyboardMarkup()

    buttons = [types.InlineKeyboardButton(btn_label, callback_data=btn_c_data)
               for btn_label, btn_c_data in buttons_labels_callback_data.items()]

    keyboard.add(*buttons)

    return keyboard


def get_priority_user_id_for_exchange(users: List, msg: types.Message):
    acceptors_users_ids = []
    for user in users:
        asses = user['assesments']
        if asses and user['user_id'] == msg.from_user.id:
            for assesm in asses:
                if assesm['sign'] == 'like':
                    acceptors_users_ids.append(assesm['user_id'])

    try:
        # Высший приоритет у последнего П-ля
        acceptors_users_id = acceptors_users_ids[-1]
    except IndexError:  # Никто не оценивал вещи П-ля
        acceptors_users_id = ''

    return acceptors_users_id


def get_priority_users_ids_for_matching(users: List, c_query: types.CallbackQuery):
    donor_id = c_query.from_user.id
    acceptors_users_ids = []
    for user in users:
        asses = user['assesments']
        if asses and user['user_id'] == donor_id:
            for assesm in asses:
                if assesm['sign'] == 'like':
                    acceptors_users_ids.append(assesm['user_id'])
    
    donors_acceptors = get_combinations_of_users(donor_id, acceptors_users_ids)

    donors_users_ids = []
    for acceptors_user_id in acceptors_users_ids:
        for user_ in users:
            if user_['user_id'] == acceptors_user_id:
                for assesment in user_['assesments']:
                    if assesment['sign'] == 'like':
                        donors_users_ids.append(assesment['user_id'])

    donor, _ = get_user_and_users_field(users, c_query.message.photo[-1].file_unique_id)
    acceptors_donors = get_combinations_of_users(donor['user_id'], donors_users_ids)

    return donors_acceptors, acceptors_donors  # Ещё вернуть donor['user_id'] для отправки контактов


def get_combinations_of_users(donor_id, acceptors_ids: List, combinations_of_users=None) -> List[Tuple[int, int]]:
    combinations_of_users = combinations_of_users or []
    for acceptors_id in acceptors_ids:
        combinations_of_users.append((donor_id, acceptors_id, ))

    return combinations_of_users


def is_users_match(donors_acceptors: List, acceptors_donors: List):
    for acceptor, donor in acceptors_donors:
        return (donor, acceptor) in donors_acceptors
