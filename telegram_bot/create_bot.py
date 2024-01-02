from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from dotenv import load_dotenv, find_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)