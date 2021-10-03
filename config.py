from typing import Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_GOODS_PHOTO_DIR: str

    USERS_OBJ_FIELDS: Tuple[str, str, str, str]
    ASSESMENTS_OBJ_FIELDS: Tuple[str, str, str]
    SHELVE_FILENAME: str

    BOTS_TEST_CMD: str
    BOTS_START_CMD: str
    BOTS_ADD_STUFF_CMD: str
    BOTS_SEARCH_CMD: str
    BOTS_EXCHANGE_CMD: str
    BOTS_HELP_CMD: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


codes_states = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',

]
messages_texts = [
    '''Добавьте фото вещи, нажав на значок "скрепки", без добавления подписи к нему;
    следующим сообщением, напишите название вещи''',

    'Ваша оценка учтена!',
    'Начните пользоваться ботом командой /add_stuff',
    'Недостаточно пользователей в хранилище для показа вещей',
    'Вы стали приоритетным пользователем для пользователя с user_id: {}',
    'Название вещи добавлено в хранилище',
    'Совпадение в желаниях к обмену найдено!',
    'Напишите пользователю @{} для согласования обмена',

    '''Привет! Я помогу вам обменять что-то ненужное на очень нужное.
    Чтобы разместить вещь к обмену загрузите её фото и укажите короткое название.
    После этого вам станут доступны вещи других пользователей.
    Для получения подробной информации напишите /help.''',
    'Фото вещи добавлено в хранилище'
    
]
messages_per_states_codes = dict(zip(codes_states, messages_texts))

buttons_labels = ['❤️', '💔', '🔚', ]
buttons_callback_data = ['like', 'dislike', 'exit', ]
buttons_labels_callback_data = dict(zip(buttons_labels, buttons_callback_data))

commands = {  
    'start': 'Описание работы с ботом',
    'add_stuff': 'Добавить вещь',
    'search_stuff': 'Найти вещь',
    'exchange_stuff': 'Обменять вещь',
    'help': 'Доступные команды для бота',
}
