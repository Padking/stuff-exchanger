from pydantic import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str

    BOT_TEST_CMD: str
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
