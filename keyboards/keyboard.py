from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
import emoji

b1 = InlineKeyboardButton(emoji.emojize(':house:'))
b2 = InlineKeyboardButton('Символы', callback_data='Символы')
b3 = InlineKeyboardButton('Подземелья', callback_data='Подземелье')
b4 = InlineKeyboardButton('Баннер', callback_data='Баннер')
b5 = InlineKeyboardButton('Гео', callback_data='Symb_geo')
b6 = InlineKeyboardButton('Дендро', callback_data='Symb_dendro')
b7 = InlineKeyboardButton('Крио', callback_data='Symb_cryo')
b8 = InlineKeyboardButton('Пиро', callback_data='Symb_pyro')
b9 = InlineKeyboardButton('Гидро', callback_data='Symb_hydro')
b10 = InlineKeyboardButton('Электро', callback_data='Symb_electro')
b11 = InlineKeyboardButton('Анемо', callback_data='Symb_anemo')


kb = InlineKeyboardMarkup(resize_keyboard=True).add(b2).add(b3, b4)

symbs = InlineKeyboardMarkup(resize_keyboard=True).row(b5, b6).row(b7, b8, b9).row(b10, b11)
