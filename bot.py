import logging

from aiogram import (
    Bot, Dispatcher,
    executor, types
)
from aiogram.dispatcher.filters import Text

import bots_helper
import config
import utils
import keyboards as kb

def main():

    @dp.message_handler(commands="start")
    async def start_cmd(message: types.Message):
        text_msg = config.messages_per_states_codes.get('1')
        await message.answer(text_msg)

    @dp.message_handler(commands="help")
    async def help_cmd(message: types.Message):
        text_msg = config.messages_per_states_codes.get('3')
        await message.answer(text_msg, reply_markup=kb.find_goods_kb)

    @dp.message_handler(commands="add_stuff")
    async def help_cmd(message: types.Message):
        text_msg = 'Загрузите фото'
        await message.answer(text_msg, reply_markup=kb.find_goods_kb)
        @dp.message_handler(content_types=types.message.ContentType.PHOTO)
        async def add_stuff(message):
            await message.photo[-1].download(destination_dir=constants.TELEGRAM_GOODS_PHOTO_DIR)
            users = utils.get_users()
            utils.update_users(users, message)
            await message.answer('Фото загружено')

    '''
   @dp.message_handler(content_types=types.message.ContentType.PHOTO)
    async def add_stuff(message):
        await message.photo[-1].download(destination_dir=constants.TELEGRAM_GOODS_PHOTO_DIR)
        users = utils.get_users()
        utils.update_users(users, message)
        await message.answer('Фото загружено')
'''

    @dp.message_handler(commands=constants.BOTS_SEARCH_CMD)
    async def search_stuff_cmd(message: types.Message):
        good = utils.get_good(message.from_user.id)
        await message.answer_photo(good['image']['file_id'], caption=good['name'],
                                   reply_markup=bots_helper.get_keyboard())


    @dp.callback_query_handler(Text(equals=config.buttons_callback_data[:2]))
    async def add_assesment_to_db(callback_query: types.CallbackQuery):
        # Добавление инфы в БД
        text_msg = config.messages_per_states_codes.get('2')
        await callback_query.answer(text=text_msg, show_alert=True)


if __name__ == '__main__':
    constants = config.Settings()

    bot = Bot(token=constants.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)

    main()

    executor.start_polling(dp, skip_updates=True)
