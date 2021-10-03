import logging

from aiogram import (
    Bot, Dispatcher,
    executor, types
)
from aiogram.dispatcher.filters import Text

import bots_helper
import config
import entities_worker
import utils


def main():

    @dp.message_handler(commands=constants.BOTS_ADD_STUFF_CMD)
    async def add_stuff_cmd(message: types.Message):
        text_msg = config.messages_per_states_codes.get('1')
        await message.answer(text_msg)


    @dp.message_handler(content_types=types.message.ContentType.PHOTO)
    async def add_stuffs_photo(message: types.Message):
        await message.photo[-1].download(destination_dir=constants.TELEGRAM_GOODS_PHOTO_DIR)
        users = utils.get_users()
        user = utils.update_users(users, message)
        utils.update_goods(users, user, message)


    @dp.message_handler(commands=constants.BOTS_SEARCH_CMD)
    async def search_stuff_cmd(message: types.Message):
        user_id = message.from_user.id
        users = utils.get_users()
        user = entities_worker.search_user(users, user_id)

        users_id_ready_to_exchange = bots_helper.get_priority_user_id_for_exchange(users, message)

        if not user:
            text_msg = config.messages_per_states_codes.get('3')
            await message.reply(text_msg)
        elif len(users) == 1:
            text_msg = config.messages_per_states_codes.get('4')
            await message.reply(text_msg)
        elif users_id_ready_to_exchange:
            good = entities_worker.get_good(users, users_id_ready_to_exchange)
            await message.answer_photo(good['image']['file_id'], caption=good['name'],
                                       reply_markup=bots_helper.get_keyboard())
        else:
            good = entities_worker.get_random_good(users, user_id)
            await message.answer_photo(good['image']['file_id'], caption=good['name'],
                                       reply_markup=bots_helper.get_keyboard())


    @dp.callback_query_handler(Text(equals=config.buttons_callback_data[:2]))
    async def add_assesment_to_db(callback_query: types.CallbackQuery):
        # Запись оценки в БД
        users = utils.get_users()
        utils.update_assesments(users, callback_query)

        users = utils.get_users()
        donors_acceptors, acceptors_donors = bots_helper.get_priority_users_ids_for_matching(users, callback_query)
        users_match_exist = bots_helper.is_users_match(donors_acceptors, acceptors_donors)
        if users_match_exist:
            # Прислать контакты донора акцептору, а акцептора донору
            await callback_query.answer('Совпадение найдено!')

        text_msg = config.messages_per_states_codes.get('2')
        await callback_query.answer(text=text_msg, show_alert=True)


    @dp.message_handler(commands=constants.BOTS_EXCHANGE_CMD)
    async def exchange_stuff(message: types.Message):
        users = utils.get_users()
        priority_user_for_exchange = bots_helper.get_priority_user_id_for_exchange(users, message)
        text_msg_template = config.messages_per_states_codes.get('5')
        text_msg = text_msg_template.format(priority_user_for_exchange)
        await message.answer(text_msg)


    @dp.message_handler()
    async def add_stuffs_name(message: types.Message):
        users = utils.get_users()
        utils.update_goods_name(users, message)
        text_msg = config.messages_per_states_codes.get('6')
        await message.answer(text_msg)


if __name__ == '__main__':
    constants = config.Settings()

    bot = Bot(token=constants.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)

    main()

    executor.start_polling(dp, skip_updates=True)
