from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from DataBase import mysql_db
from keyboards import kb, symbs
import datetime
import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    res1 = await mysql_db.sql_readMenu("help1")
    res2 = await mysql_db.sql_readMenu("help2")
    res3 = await mysql_db.sql_readMenu("help3")
    media_group = types.MediaGroup()
    media_group.attach_photo(res1[0][0], f'{res1[0][2]}')
    media_group.attach_photo(res2[0][0])
    await message.answer_media_group(media=media_group)
    await message.answer_photo(res3[0][0], f'Альтернативный способ просмотреть страницу пользователя', reply_markup=InlineKeyboardMarkup()
                               .add(InlineKeyboardButton(text="Вернуться на главную", callback_data='home')))


#@dp.message_handler(commands=['start', 'home'])
async def command_start(message: types.Message):
    result = await mysql_db.sql_readMenu("welcome_page")
    await message.answer_photo(result[0][0], f'{result[0][2]}', parse_mode=types.ParseMode.HTML, reply_markup=kb)
    await message.delete()


#@dp.message_handler(Text(equals='home'))
async def command_start1(call: types.CallbackQuery):
    result = await mysql_db.sql_readMenu("welcome_page")
    await call.message.answer_photo(result[0][0], f'{result[0][2]}', parse_mode=types.ParseMode.HTML, reply_markup=kb)


#@dp.message_handler(Text(equals='Символы'))
async def command_symbol1(message: types.Message):
    result = await mysql_db.sql_readMenu("symbols_main")
    await message.answer_photo(result[0][0], f'{result[0][2]}', parse_mode=types.ParseMode.HTML, reply_markup=symbs)

#@dp.message_handler(Text(equals='Символы'))
async def command_symbol(call: types.CallbackQuery):
    result = await mysql_db.sql_readMenu("symbols_main")
    await call.message.answer_photo(result[0][0], f'{result[0][2]}', parse_mode=types.ParseMode.HTML, reply_markup=symbs)


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('prop_'))
async def prop(call: types.CallbackQuery):
    result = await mysql_db.sql_readProp(call.data.replace("prop_", ""))
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'{i[1]}')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('set_'))
async def set(call: types.CallbackQuery):
    result = await mysql_db.sql_readArt(call.data.replace("set_", ""))
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'{i[1]}')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('weap_'))
async def weap(call: types.CallbackQuery):
    result = await mysql_db.sql_readWeap(call.data.replace("weap_", ""))
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'{i[1]}')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('team_'))
async def teams(call: types.CallbackQuery):
    result = await mysql_db.sql_readTeams(call.data.replace("team_", ""))
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'{i[1]}')))


#@dp.message_handler(Text(equals='Аяка'))
async def ayaka_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Аяка")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аяка'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аяка'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аяка'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аяка'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#dp.callback_query_handler(Text(equals='Аяка'))
async def ayaka_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Аяка")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аяка'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аяка'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аяка'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аяка'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Альбедо'))
async def albedo_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Альбедо")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Альбедо'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Альбедо'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Альбедо'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Альбедо'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#dp.callback_query_handler(Text(equals='Альбедо'))
async def albedo_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Альбедо")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Альбедо'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Альбедо'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Альбедо'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Альбедо'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Аль-Хайтам'))
async def alhaitam_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Аль-Хайтам")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аль-Хайтам'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аль-Хайтам'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аль-Хайтам'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аль-Хайтам'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Аль-Хайтам'))
async def alhaitam_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Аль-Хайтам")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аль-Хайтам'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аль-Хайтам'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аль-Хайтам'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аль-Хайтам'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))



#@dp.message_handler(Text(equals='Аято'))
async def ayato_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Аято")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аято'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аято'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аято'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аято'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Аято'))
async def ayato_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Аято")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Аято'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Аято'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Аято'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Аято'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))



#@dp.message_handler(Text(equals='Райдэн'))
async def baal_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Райдэн")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Райдэн'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Райдэн'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Райдэн'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Райдэн'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Райдэн'))
async def baal_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Райдэн")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Райдэн'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Райдэн'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Райдэн'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Райдэн'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Бай Чжу'))
async def baych_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Бай_Чжу")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'Supp_prop_Бай_Чжу'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'Supp_prop_Бай_Чжу'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'Supp_weap_Бай_Чжу'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Бай_Чжу'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Бай_Чжу'))
async def baych_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Бай_Чжу")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'Supp_prop_Бай_Чжу'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'Supp_prop_Бай_Чжу'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'Supp_weap_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Supp_prop_'))
async def baychsupp_prop(call: types.CallbackQuery):
    result = await mysql_db.sql_readProp("Бай_Чжу_Сапп")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саб-дд билд", callback_data=f'Subdd_prop_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))

#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Subdd_prop_'))
async def baychsubdd_prop(call: types.CallbackQuery):
    result = await mysql_db.sql_readProp("Бай_Чжу_Сабдд")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саппорт билд", callback_data=f'Supp_prop_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))

#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Supp_set'))
async def baychsupp_set(call: types.CallbackQuery):
    result = await mysql_db.sql_readArt("Бай_Чжу_Сапп")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саб-дд билд", callback_data=f'Subdd_set_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Subdd_set'))
async def baychsubdd_set(call: types.CallbackQuery):
    result = await mysql_db.sql_readArt("Бай_Чжу_Сабдд")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саппорт билд", callback_data=f'Supp_set_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))



#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Supp_weap_'))
async def baychsupp_weap(call: types.CallbackQuery):
    result = await mysql_db.sql_readWeap("Бай_Чжу_Сапп")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саб-дд билд", callback_data=f'Subdd_weap_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Subdd_weap_'))
async def baychsubdd_weap(call: types.CallbackQuery):
    result = await mysql_db.sql_readArt("Бай_Чжу_Сабдд")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Просмотреть саппорт билд", callback_data=f'Supp_weap_Бай_Чжу'))
                                        .add(InlineKeyboardButton(text="Назад", callback_data=f'Бай_Чжу')))


#@dp.message_handler(Text(equals='Ёимия'))
async def yomiya_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Ёимия")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Ёимия'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Ёимия'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Ёимия'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Ёимия'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Ёимия'))
async def yomiya_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Ёимия")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Ёимия'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Ёимия'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Ёимия'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Ёимия'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Лайла'))
async def layla_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Лайла")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Лайла'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Лайла'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Лайла'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Лайла'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Лайла'))
async def layla_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Лайла")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Лайла'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Лайла'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Лайла'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Лайла'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Син Цю'))
async def sin_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Син_Цю")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Син_Цю'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Син_Цю'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Син_Цю'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Син_Цю'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Син_Цю'))
async def sin_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Син_Цю")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Син_Цю'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Син_Цю'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Син_Цю'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Син_Цю'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Ху Тао'))
async def hu_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Ху_Тао")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Ху_Тао'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Ху_Тао'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Ху_Тао'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Ху_Тао'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Ху_Тао'))
async def hu_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Ху_Тао")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Ху_Тао'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Ху_Тао'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Ху_Тао'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Ху_Тао'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Яэ Мико'))
async def miko_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Яэ_Мико")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Яэ_Мико'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Яэ_Мико'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Яэ_Мико'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Яэ_Мико'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Яэ_Мико'))
async def miko_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Яэ_Мико")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Яэ_Мико'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Яэ_Мико'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Яэ_Мико'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Яэ_Мико'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Юнь Цзинь'))
async def yun_ch(message: types.Message):
    result = await mysql_db.sql_readCh("Юнь_Цзинь")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Юнь_Цзинь'))
                                   .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Юнь_Цзинь'),
                                        InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Юнь_Цзинь'))
                                   .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Юнь_Цзинь'))
                                   .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.callback_query_handler(Text(equals='Юнь_Цзинь'))
async def yun_char(call: types.CallbackQuery):
    result = await mysql_db.sql_readCh("Юнь_Цзинь")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text="Рекомендуемые значения характеристик", callback_data=f'prop_Юнь_Цзинь'))
                                        .row(InlineKeyboardButton(text="Лучшие артефакты", callback_data=f'set_Юнь_Цзинь'),
                                             InlineKeyboardButton(text="Лучшее оружие", callback_data=f'weap_Юнь_Цзинь'))
                                        .add(InlineKeyboardButton(text="Примеры группы", callback_data=f'team_Юнь_Цзинь'))
                                        .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Баннер'))
async def command_banner1(message: types.Message):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("персонаж")
    for i in result:
        await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                   .add(InlineKeyboardButton(text='Молитва события персонажа II', callback_data=f'2_персонаж'))
                                   .add(InlineKeyboardButton(text='Молитва события оружия', callback_data=f'оружие'))
                                   .add(InlineKeyboardButton(text='Стандартная молитва', callback_data=f'стандарт')))
    await message.answer(text=f'<i>До конца баннера осталось {delta.days} дн., {delta.seconds // 3600} ч.</i>',
                         parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                         .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#@dp.message_handler(Text(equals='Баннер'))
async def command_banner(call: types.CallbackQuery):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("персонаж")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text='Молитва события персонажа II', callback_data=f'2_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события оружия', callback_data=f'оружие'))
                                        .add(InlineKeyboardButton(text='Стандартная молитва', callback_data=f'стандарт')))
    await call.message.answer(text=f'<i>До конца баннера осталось {delta.days} дн., {delta.seconds // 3600} ч.</i>',
                              parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                              .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('2_'))
async def char2_callback(call: types.CallbackQuery):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("персонаж_2")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text='Молитва события персонажа',callback_data=f'1_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события оружия', callback_data=f'оружие'))
                                        .add(InlineKeyboardButton(text='Стандартная молитва', callback_data=f'стандарт')))
    await call.message.answer(text=f'<i>До конца баннера осталось {delta.days} дн., {delta.seconds // 3600} ч.</i>',
                              parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                              .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#@dp.callback_query_handler(lambda x: x.data and x.data.startswith('1_'))
async def char_callback(call: types.CallbackQuery):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("персонаж")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text='Молитва события персонажа II', callback_data=f'2_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события оружия', callback_data=f'оружие'))
                                        .add(InlineKeyboardButton(text='Стандартная молитва', callback_data=f'стандарт')))
    await call.message.answer(text=f'<i>До конца баннера осталось {delta.days} дн., {delta.seconds // 3600} ч.</i>',
                              parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                              .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('оружие'))
async def weap_callback(call: types.CallbackQuery):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("оружие")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text='Молитва события персонажа', callback_data=f'1_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события персонажа II', callback_data=f'2_персонаж'))
                                        .add(InlineKeyboardButton(text='Стандартная молитва', callback_data=f'стандарт')))
    await call.message.answer(text=f'<i>До конца баннера осталось {delta.days} дн., {delta.seconds // 3600} ч.</i>',
                              parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                              .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('стандарт'))
async def standart_callback(call: types.CallbackQuery):
    delta = datetime.datetime(2023, 5, 23, 16) - datetime.datetime.now()
    result = await mysql_db.sql_readMenu("жажда_странствий")
    for i in result:
        await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                        .add(InlineKeyboardButton(text='Молитва события персонажа', callback_data=f'1_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события персонажа II', callback_data=f'2_персонаж'))
                                        .add(InlineKeyboardButton(text='Молитва события оружия', callback_data=f'оружие')))
    await call.message.answer(text=f'Баннер бессрочный', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                              .add(InlineKeyboardButton(text='Вернуться на главную', callback_data=f'home')))


#@dp.message_handler(Text(equals='Подземелья'))
async def command_dungeon1(message: types.Message):
    now = datetime.datetime.now()
    weekday = datetime.datetime.isoweekday(now)
    if weekday == 1 or weekday == 4:
        k = await mysql_db.sql_readMenu("понедельник")
        for i in k:
            await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                       .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif weekday == 2 or weekday == 5:
        k = await mysql_db.sql_readMenu("вторник")
        for i in k:
            await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                       .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif weekday == 3 or weekday == 6:
        k = await mysql_db.sql_readMenu("среда")
        for i in k:
            await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                       .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    else:
        k = await mysql_db.sql_readMenu("воскресенье")
        for i in k:
            await message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                       .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#@dp.message_handler(Text(equals='Подземелья'))
async def command_dungeon(call: types.CallbackQuery):
    now = datetime.datetime.now()
    weekday = datetime.datetime.isoweekday(now)
    if weekday == 1 or weekday == 4:
        k = await mysql_db.sql_readMenu("понедельник")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif weekday == 2 or weekday == 5:
        k = await mysql_db.sql_readMenu("вторник")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif weekday == 3 or weekday == 6:
        k = await mysql_db.sql_readMenu("среда")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    else:
        k = await mysql_db.sql_readMenu("воскресенье")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('Symb_'))
async def symb_callback(call: types.CallbackQuery):
    if call.data.replace("Symb_", "") == "geo":
        k = await mysql_db.sql_readMenu("Гео_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "dendro":
        k = await mysql_db.sql_readMenu("Дендро_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "cryo":
        k = await mysql_db.sql_readMenu("Крио_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "pyro":
        k = await mysql_db.sql_readMenu("Пиро_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "electro":
        k = await mysql_db.sql_readMenu("Электро_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "anemo":
        k = await mysql_db.sql_readMenu("Анемо_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))
    elif call.data.replace("Symb_", "") == "hydro":
        k = await mysql_db.sql_readMenu("Гидро_персонажи")
        for i in k:
            await call.message.answer_photo(i[0], f'{i[2]}', parse_mode=types.ParseMode.HTML, reply_markup=InlineKeyboardMarkup()
                                            .add(InlineKeyboardButton(text="Вернуться на главную", callback_data=f'home')))


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'home'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_symbol1, commands=['symbs'])
    dp.register_message_handler(command_dungeon1, commands=['dung'])
    dp.register_message_handler(command_banner1, commands=['banner'])
    dp.register_message_handler(ayaka_ch, Text(equals='Аяка'))
    dp.register_message_handler(albedo_ch, Text(equals='Альбедо'))
    dp.register_message_handler(alhaitam_ch, Text(equals='Аль-Хайтам'))
    dp.register_message_handler(ayato_ch, Text(equals='Аято'))
    dp.register_message_handler(baal_ch, Text(equals='Райдэн'))
    dp.register_message_handler(baych_ch, Text(equals='Бай Чжу'))
    dp.register_message_handler(yomiya_ch, Text(equals='Ёимия'))
    dp.register_message_handler(layla_ch, Text(equals='Лайла'))
    dp.register_message_handler(sin_ch, Text(equals='Син Цю'))
    dp.register_message_handler(hu_ch, Text(equals='Ху Тао'))
    dp.register_message_handler(yun_ch, Text(equals='Юнь Цзинь'))
    dp.register_message_handler(miko_ch, Text(equals='Яэ Мико'))
    dp.register_callback_query_handler(command_banner, lambda x: x.data and x.data.startswith('Баннер'))
    dp.register_callback_query_handler(command_symbol, lambda x: x.data and x.data.startswith('Символы'))
    dp.register_callback_query_handler(command_dungeon, lambda x: x.data and x.data.startswith('Подземелье'))
    dp.register_callback_query_handler(prop, lambda x: x.data and x.data.startswith('prop_'))
    dp.register_callback_query_handler(weap, lambda x: x.data and x.data.startswith('weap_'))
    dp.register_callback_query_handler(set, lambda x: x.data and x.data.startswith('set_'))
    dp.register_callback_query_handler(teams, lambda x: x.data and x.data.startswith('team_'))
    dp.register_callback_query_handler(baychsupp_prop, lambda x: x.data and x.data.startswith('Supp_prop_'))
    dp.register_callback_query_handler(baychsubdd_prop, lambda x: x.data and x.data.startswith('Subdd_prop_'))
    dp.register_callback_query_handler(baychsupp_set, lambda x: x.data and x.data.startswith('Supp_set_'))
    dp.register_callback_query_handler(baychsubdd_set, lambda x: x.data and x.data.startswith('Subdd_set_'))
    dp.register_callback_query_handler(baychsupp_weap, lambda x: x.data and x.data.startswith('Supp_weap_'))
    dp.register_callback_query_handler(baychsubdd_weap, lambda x: x.data and x.data.startswith('Subdd_weap_'))
    dp.register_callback_query_handler(command_start1, Text(equals='home'))
    dp.register_callback_query_handler(ayaka_char, Text(equals='Аяка'))
    dp.register_callback_query_handler(albedo_char, Text(equals='Альбедо'))
    dp.register_callback_query_handler(alhaitam_char, Text(equals='Аль-Хайтам'))
    dp.register_callback_query_handler(ayato_char, Text(equals='Аято'))
    dp.register_callback_query_handler(baal_char, Text(equals='Райдэн'))
    dp.register_callback_query_handler(baych_char, Text(equals='Бай_Чжу'))
    dp.register_callback_query_handler(yomiya_char, Text(equals='Ёимия'))
    dp.register_callback_query_handler(layla_char, Text(equals='Лайла'))
    dp.register_callback_query_handler(sin_char, Text(equals='Син_Цю'))
    dp.register_callback_query_handler(hu_char, Text(equals='Ху_Тао'))
    dp.register_callback_query_handler(yun_char, Text(equals='Юнь_Цзинь'))
    dp.register_callback_query_handler(miko_char, Text(equals='Яэ_Мико'))
    dp.register_callback_query_handler(char_callback, lambda x: x.data and x.data.startswith('1_'))
    dp.register_callback_query_handler(char2_callback, lambda x: x.data and x.data.startswith('2_'))
    dp.register_callback_query_handler(weap_callback, lambda x: x.data and x.data.startswith('оружие'))
    dp.register_callback_query_handler(standart_callback, lambda x: x.data and x.data.startswith('стандарт'))
    dp.register_callback_query_handler(symb_callback, lambda x: x.data and x.data.startswith('Symb_'))

