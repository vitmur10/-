import aiogram
from Const import API_TOKEN
import keyboard

# Initialize bot and dispatcher
bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'], content_types=['text'])
async def hello(message: aiogram.types.Message):
    await message.answer("Привіт👋 наш майбутній гравець.\nДякую що обрав нас🙏.\n"
                         "Почнемо твоє посвячення у нашу дружню сім'ю👨‍👨‍👦...", reply_markup=keyboard.keyboard_start)


@dp.message_handler(content_types=['text'])
async def one(message: aiogram.types.Message):
    if message.text == 'Як до вас приєднатися':
        await message.answer("Почнемо твоє посвячення у"
                             " нашу дружню сім'ю👨‍👨‍👦...", reply_markup=keyboard.keyboard_start)
    elif message.text == 'Почали':
        await message.answer('Для початку завантаж клієнт\n'
                             'Як завантавижиш продовжимо...', reply_markup=keyboard.keyboard1)
    elif message.text == "️▶️Продовжити▶️":
        await message.answer('Тепер завантаж наш сервер\nЯк завантавижиш продовжимо...', reply_markup=keyboard.keyboard2)
    elif message.text == "✅Готово✅":
        await message.answer('Вітаю🥳\nТи став частининою нашої сімї\nПриємної гри', reply_markup=keyboard.keyboard_menu)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)