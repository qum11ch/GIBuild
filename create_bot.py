from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6194043101:AAENDQGyy9WefgwZQbFU9ivDke1GBWSjNWs')
dp = Dispatcher(bot, storage=storage)
