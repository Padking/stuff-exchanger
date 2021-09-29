from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_USERS_GOODS_FILE: str
    TELEGRAM_GOODS_PHOTO_DIR: str

    BOTS_TEST_CMD: str
    BOTS_ADD_STUFF_CMD: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


codes_states = ['1', ]
messages_texts = [
    'Добавьте фото и название вещи',

]

messages_per_states_codes = dict(zip(codes_states, messages_texts))
