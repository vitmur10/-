import aiogram
from main import bot, dp

#Кнопка почали
keyboard_start = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_3 = aiogram.types.KeyboardButton(text="Почали")
keyboard_start.add(button_3)

#Кнопка меню
keyboard_menu = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_donat = aiogram.types.KeyboardButton(text="💰Поповнити баланс💰")
button_site = aiogram.types.KeyboardButton(text="Перейти на сайт")
button_forum = aiogram.types.KeyboardButton(text="Перейти на форум")
button_rating = aiogram.types.KeyboardButton(text='🔝Переглянути рейтинг🔝')
button_join = aiogram.types.KeyboardButton(text='Як до вас приєднатися')
fs = [button_site, button_forum]
rd = [button_rating, button_donat]
keyboard_menu.add(button_join, *fs, *rd)

#Кнопка продовжити

keyboard1 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = aiogram.types.KeyboardButton(text="️▶️Продовжити▶️")
keyboard1.add(button_1)

#Кнопка готово
keyboard2 = aiogram.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_2 = aiogram.types.KeyboardButton(text="✅Готово✅")
keyboard2.add(button_2)