import telebot
from telebot import types


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.chat.id
    referred_by = message.text.split('_')[1] if '_' in message.text else None
    if referred_by:
        referrer_id = referral_codes.get(referred_by)
        if referrer_id:
            bot.send_message(referrer_id, f'Поздравляю, вы приглосили пользователя за это вам начислят  {user_id}')
            # тута награда челика который пригласил реферала своего
    else:
        bot.reply_to(message, 'Привет!')

@bot.message_handler(func=lambda message: message.text.lower() == 'Реферальная система')
def generate_referral_link(message):
    user_id = message.chat.id
    referral_code = str(user_id)
    referral_codes[referral_code] = user_id
    bot.reply_to(message, f'Ваша ссылка: t.me/qweton_bot?start={referral_code}')