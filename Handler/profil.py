import sqlite3

from aiogram import Router
from aiogram.types import Message

router = Router()

async def get_user_by_id(DB, id_user):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute('''SELECT * FROM User WHERE id_user = ?''', (id_user,))
        user = cursor.fetchone()
        return user
    finally:
        conn.close()

@router.message()
async def profile_handler(msg: Message):
    user_id = msg.from_user.id

    if msg.text.lower() == 'профиль':
        DB = 'User_Info.db'
        user_info = await get_user_by_id(DB, user_id)
        if user_info:
            await msg.answer(f'Информация:\n\nВаш айди: {user_info[1]}\nБаланс: {user_info[2]}\nРефералов: {user_id[3]}\nКошелёк: {user_info[4]}')
        else:
            pass