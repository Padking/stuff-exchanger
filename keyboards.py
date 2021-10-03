from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


add_item_button = KeyboardButton("Добавить вещь")
find_item_button = KeyboardButton("Найти вещь")
exchange_offer_button = KeyboardButton("Предложить обмен")


find_goods_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(find_item_button)
user_with_items_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(add_item_button, find_item_button)

