import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

API_TOKEN = '6392514625:AAFymeOXq450T04_m-prC-D5VYTQA2dBNGE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

balans = 0
ref = 0
crypto_wallet = []


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    chat_id = '-1002084767114'
    member = await bot.get_chat_member(chat_id, user_id)

    if member.status in ['member', 'creator']:
        keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Профиль')
        btn2 = types.KeyboardButton('Криптокошелек')
        btn3 = types.KeyboardButton('Реферальная система')
        keyboard_markup.add(btn1, btn2)
        keyboard_markup.add(btn3)

        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton('Реферал', callback_data='invite'))

        await message.answer('Привет! Добро пожаловать!', reply_markup=keyboard_markup)
    else:
        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton('Join QWETON', url='https://t.me/+OsklCmoqvCRkOWJi'))
        await message.answer('Чтобы участвовать в AIRDROP, Вам необходимо сначала подписаться на следующие каналы 👇', reply_markup=inline_markup)

@dp.message_handler()
async def profil(message: types.Message):
    if message.text.lower() == 'профиль':
        await message.answer(f'Информация профиля: \n Баланс: {balans} $QWT \n Количество рефералов: {ref}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


#6392514625:AAFymeOXq450T04_m-prC-D5VYTQA2dBNGE