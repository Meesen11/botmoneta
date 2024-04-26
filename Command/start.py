import logging
import sqlite3

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.methods import GetChat
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

async def insert_user(DB, id_user, balans, referals, wallet):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO User (id_user, balans, referals, wallet) VALUES (?, ?, ?, ?)''',
                       (id_user, balans, referals, wallet))
        conn.commit()
        logging.info("Пользователь добавлен в базу данных")
    except sqlite3.IntegrityError:
        logging.error("Пользователь с таким id_user уже существует в базе данных")
    finally:
        conn.close()

async def update_referals(DB, id_user):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT referals FROM User WHERE id_user = ?''', (id_user,))
        current_referals = cursor.fetchone()[0]
        
        new_referals = current_referals + 1

        cursor.execute('''UPDATE User SET referals = ? WHERE id_user = ?''', (new_referals, id_user))
        conn.commit()
        logging.info("Количество рефералов пользователя обновлено")
    except sqlite3.Error as e:
        logging.error("Ошибка при обновлении количества рефералов пользователя:", e)
    finally:
        conn.close()

@router.message(Command("start"))
async def start_cmd(msg: Message, bot: Bot):
    user_id = msg.from_user.id

    user = await bot(GetChat(chat_id=user_id))
    username = user.username

    chat_id = '-1002084767114'
    DB = 'User_Info.db'

    await insert_user(DB, user_id, 0, 0, "None")
    
    text_parts = msg.text.split()
    if len(text_parts) > 1:
        creator_ref = text_parts[1]

        if user_id != creator_ref:
            user_ref = await bot(GetChat(chat_id=creator_ref))
            username_ref = user_ref.username

            text_referral = f"Поздравляю, вы стали рефералом @{username_ref}"
            text_new_referral = f"Пользователь @{username} присоединился к боту по вашей ссылке."
            await msg.answer(text=text_referral)
            await bot.send_message(creator_ref, text_new_referral)
            await update_referals(DB, creator_ref)
        else:
            text_referral_creator = "Извините, но вы не можете быть своим рефералом!"
            await msg.answer(text=text_referral_creator)
    else:
        member = await bot.get_chat_member(chat_id, user_id)
        if member.status in ['member', 'creator']:
            kb = [
                [KeyboardButton(text="Профиль")], 
                [KeyboardButton(text="Криптокошелек")],
                [KeyboardButton(text="'Реферальная система ")]
            ]
            keyboard = ReplyKeyboardMarkup(keyboard=kb)

            await msg.answer('Привет! Добро пожаловать!', reply_markup=keyboard)
        else:
            builder = InlineKeyboardBuilder()
            builder.add(InlineKeyboardButton(
                text="Нажми меня",
                url="https://t.me/+OsklCmoqvCRkOWJi")
            )
            await msg.answer('Чтобы участвовать в AIRDROP, Вам необходимо сначала подписаться на следующие каналы 👇', reply_markup=builder.as_markup())

@router.message(Command("ref"))
async def ref_cmd(msg: Message):
    user_id = msg.from_user.id
    name_bot = 'qweton_bot' # Юзер нейм бота без (@)
    URL_BOT = f'https://t.me/{name_bot}?start={user_id}'

    text_send_URL = f"Ваша реферальная ссылка: {URL_BOT}"
    await msg.answer(text=text_send_URL)
