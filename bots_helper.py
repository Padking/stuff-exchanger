from typing import Dict

from aiogram import types

from config import buttons_labels_callback_data


def get_keyboard(buttons_labels_callback_data: Dict=buttons_labels_callback_data, buttons=None):

    buttons = buttons or []
    keyboard = types.InlineKeyboardMarkup()

    buttons = [types.InlineKeyboardButton(btn_label, callback_data=btn_c_data)
               for btn_label, btn_c_data in buttons_labels_callback_data.items()]

    keyboard.add(*buttons)

    return keyboard
