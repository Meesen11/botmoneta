import telebot
from telebot import types

bot = telebot.TeleBot('6392514625:AAFymeOXq450T04_m-prC-D5VYTQA2dBNGE')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    chat_id = '-1002084767114'
    member = bot.get_chat_member(chat_id, user_id)  

    markup = types.InlineKeyboardMarkup()
    if member.status == 'member' or member.status == 'creator':
        markup.add(types.InlineKeyboardButton('Реферал', callback_data='invite'))
        bot.send_message(message.chat.id, 'AIRDROP GUMMY BEAR COIN 🧸 Мы платим целых 250 $GMBR за одного приведенного друга Это самые лучшие условия для AIRDROP !', reply_markup=markup)

    
    if member.status != 'member' and member.status != 'creator':
        markup.add(types.InlineKeyboardButton('Join QWETON', url='https://t.me/+OsklCmoqvCRkOWJi'))
        bot.send_message(message.chat.id, 'Чтобы участвовать в AIRDROP, Вам необходимо сначала подписаться на следующие каналы 👇', reply_markup=markup)

bot.polling(none_stop=True)

