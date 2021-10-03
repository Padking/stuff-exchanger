from typing import Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_GOODS_PHOTO_DIR: str

    USERS_OBJ_FIELDS: Tuple[str, str]
    SHELVE_FILENAME: str

    BOTS_TEST_CMD: str
    BOTS_ADD_STUFF_CMD: str
    BOTS_SEARCH_CMD: str


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


codes_states = ['1', '2', '3']
messages_texts = [
    'Привет! Я помогу тебе обменять что-то ненужное на очень нужное. '\
    'Чтобы разместить вещь к обмену просто загрузи фото вещи с кратким описанием. '\
    'После этого тебе станут доступны вещи других пользователей. '\
    'Для получения подробной информации напиши - "/help"',

    'Ваша оценка учтена!',

    '''
    Доступные функции:

    “Добавить вещь” - что бы разместить вещь к обмену достаточно просто загрузить фото вещи с кратким описанием. После этого тебе станут доступны вещи других пользователей.

    Нажми “Найти вещь” - я пришлю тебе фотографии вещей других пользователей для обмена, еще раз нажми "Найти вещь" и я пришлю тебе следующее фото.

    Нажми “Обменяться” - если понравилась вещь, если владельцу вещи понравится что-то из твоих вещей, то я пришлю контакты вам обоим.

    "Скрыть" - если вещь не понравилась я больше не буду тебе ее показывать.
    ''',

]
messages_per_states_codes = dict(zip(codes_states, messages_texts))

buttons_labels = ['❤️', '💔', '🔚', ]
buttons_callback_data = ['like', 'dislike', 'exit', ]
buttons_labels_callback_data = dict(zip(buttons_labels, buttons_callback_data))
