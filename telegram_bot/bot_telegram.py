from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

from handlers import admin, client, other

client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
