from typing import Dict, List

from aiogram import types

from config import buttons_labels_callback_data


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
