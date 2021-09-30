import ast
import logging

from aiogram import (
    Bot, Dispatcher,
    executor, types
)


import config
import utils


def main():

    @dp.message_handler(commands=constants.BOTS_ADD_STUFF_CMD)
    async def add_stuff_cmd(message: types.Message):
        text_msg = config.messages_per_states_codes.get('1')
        await message.answer(text_msg)


    @dp.message_handler(content_types=types.message.ContentType.PHOTO)
    async def add_stuff(message):
        await message.photo[-1].download(destination_dir=constants.TELEGRAM_GOODS_PHOTO_DIR)
        users = utils.get_users()
        utils.update_users(users, message)


if __name__ == '__main__':
    constants = config.Settings()

    bot = Bot(token=constants.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)

    main()

    executor.start_polling(dp, skip_updates=True)
