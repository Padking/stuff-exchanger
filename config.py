from typing import Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_GOODS_PHOTO_DIR: str

    USERS_OBJ_FIELDS: Tuple[str, str, str]
    ASSESMENTS_OBJ_FIELDS: Tuple[str, str, str]
    SHELVE_FILENAME: str

    BOTS_TEST_CMD: str
    BOTS_ADD_STUFF_CMD: str
    BOTS_SEARCH_CMD: str
    BOTS_EXCHANGE_CMD: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


codes_states = [
    '1',
    '2',
    '3',
    '4',
    '5',

]
messages_texts = [
    'Добавьте фото и название вещи',
    'Ваша оценка учтена!',
    'Начните пользоваться ботом командой /add_stuff',
    'Недостаточно пользователей в БД для показа вещей',
    'Вы стали приоритетным П-ем для П-ля с user_id: {}',
    
]
messages_per_states_codes = dict(zip(codes_states, messages_texts))

buttons_labels = ['❤️', '💔', '🔚', ]
buttons_callback_data = ['like', 'dislike', 'exit', ]
buttons_labels_callback_data = dict(zip(buttons_labels, buttons_callback_data))
