from aiogram.utils import executor
from create_bot import dp
from handlers import user, admin
from DataBase import mysql_db


async def on_startup(_):
    print('Бот вышел в онлайн')
    await mysql_db.mysql_start()


user.register_handlers_user(dp)
admin.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
