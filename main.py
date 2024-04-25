import asyncio
import logging
import os
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from Command import start
from Handler import profil

async def create_db(DB):
    if not os.path.exists(DB):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                            id INTEGER PRIMARY KEY,
                            id_user INTEGER,
                            balans INTEGER,
                            referals INTEGER,
                            wallet TEXT
                        )''')

        conn.commit()
        conn.close()
        logging.info("База данных создана")

async def main():
    DB = 'User_Info.db'
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start.router)
    dp.include_router(profil.router)
    await create_db(DB)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())