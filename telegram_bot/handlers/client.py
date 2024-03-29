from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def commnad_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС. Напишите ему:\n https://t.me/TrainingPizzaBot')


# @dp.message_handler(commands=['Режим_работы'])
async def commnad_open_closed(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Чт с 09:00 до 18:00, Пт-Вс с 11:00 до 23:00')
    


# @dp.message_handler(commands=['Расположение'])
async def commnad_location(message: types.Message):
    await bot.send_message(message.from_user.id, 'Волл-Стрит 13г')


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)    

def  register_handler_client(dp: Dispatcher):
    dp.register_message_handler(commnad_start, commands=['start', 'help'])
    dp.register_message_handler(commnad_open_closed, commands=['Режим_работы'])
    dp.register_message_handler(commnad_location, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
