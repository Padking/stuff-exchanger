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
    async def save_photo(message):
        photo = message.photo[-1]
        await photo.download(destination_dir=constants.TELEGRAM_GOODS_PHOTO_DIR)

        users = utils.get_users(constants.TELEGRAM_USERS_GOODS_FILE)
        for user in users:
            if user['user_id'] == message.from_user.id:
                user['goods'].append({
                    'image': ast.literal_eval(str(photo)),
                    'name': message.caption
                })

        users_ = {
            'users': users
        }
        utils.update_users(users_, constants.TELEGRAM_USERS_GOODS_FILE)


if __name__ == '__main__':
    constants = config.Settings()

    bot = Bot(token=constants.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)

    main()

    executor.start_polling(dp, skip_updates=True)
