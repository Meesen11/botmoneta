import telebot
from telebot import types

bot = telebot.TeleBot('6392514625:AAFymeOXq450T04_m-prC-D5VYTQA2dBNGE')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Join QWETON', url='https://t.me/+OsklCmoqvCRkOWJi'))
    bot.send_message(message.chat.id, '💡 Чтобы участвовать в AIRDROP, Вам необходимо сначала подписаться на следующие каналы 👇', reply_markup=markup)

bot.polling(none_stop=True)
ёёё