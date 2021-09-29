import logging

from aiogram import Bot, Dispatcher, executor, types

from config import Settings


def main():

    @dp.message_handler(commands=config.BOT_TEST_CMD)
    async def cmd_test(message: types.Message):
        msg_template = 'Реакция на команду `/{}`'
        text_msg = msg_template.format(config.BOT_TEST_CMD)
        await message.reply(text_msg)


if __name__ == '__main__':
    config = Settings()

    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)

    main()

    executor.start_polling(dp, skip_updates=True)
