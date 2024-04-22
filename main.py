import telebot
from telebot import types

bot = telebot.TeleBot('6392514625:AAFymeOXq450T04_m-prC-D5VYTQA2dBNGE')

balans = 0
ref = 0
crypto_wallet = []
referral_links = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    chat_id = '-1002084767114'
    member = bot.get_chat_member(chat_id, user_id)  

    if member.status == 'member' or member.status == 'creator':
        reply_markup = types.ReplyKeyboardMarkup()

        btn1 = types.KeyboardButton(r'Профиль')
        btn2 = types.KeyboardButton(r'Криптокошелек')
        btn3 = types.KeyboardButton(r'Реферальная система')

        reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.add(btn1, btn2)
        reply_markup.add(btn3)

        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton('Реферал', callback_data='invite')) 
        bot.send_message(message.chat.id, 'AIRDROP QWETON COIN 🧸 Мы платим целых 250 $QWT за одного приведенного друга Это самые лучшие условия для AIRDROP !', reply_markup=inline_markup)
    
    if member.status != 'member' and member.status != 'creator':
        inline_markup = types.InlineKeyboardMarkup()
        inline_markup.add(types.InlineKeyboardButton('Join QWETON', url='https://t.me/+OsklCmoqvCRkOWJi'))
        bot.send_message(message.chat.id, 'Чтобы участвовать в AIRDROP, Вам необходимо сначала подписаться на следующие каналы 👇', reply_markup=inline_markup)






@bot.message_handler(content_types=['text'])
def profil(message):
    if message.text.lower() == 'профиль':
        bot.send_message(message.chat.id, f'Информация профиля: \n Баланc: {balans} $QWT \n Количество рефералов: {ref}')      

bot.polling()
