import telebot
from telebot import types


@bot.message_handler(func=lambda message: message.text.lower() == 'Профиль')
def profil(message):
    bot.reply_to(message, f'Ты пригласил: \n Твой баланс -  QWT')