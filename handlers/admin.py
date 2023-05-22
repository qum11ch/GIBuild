from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from DataBase import mysql_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

ID = None
table = None
tableShow = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()


#Получаем ID текущего модератора
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что вы хотите сделать?', reply_markup=admin_kb.button_case_admin)
    await message.delete()


#@dp.message_handler(Text(equals='Показать загруженное'))
async def cm_show(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id, 'В чем показать загруженное?', reply_markup=admin_kb.button_case_admin4)
        await message.delete()


#dp.callback_query_handler(lambda y: y.data and y.data.startswith('show_'))
async def show_callback_run(call: types.CallbackQuery):
    read = await mysql_db.sql_read2(call.data.replace("show_", ""))
    result = await asyncio.gather(read)
    for i in result:
        for x in i:
            await call.message.answer_photo(x[0], f'Название:\n{x[1]}\nОписание:\n{x[2]}', parse_mode=types.ParseMode.HTML)


#@dp.message_handler(Text(equals='Удалить'))
async def cm_delete(message: types.Message):
    if message.from_user.id == ID:
        await bot.send_message(message.from_user.id, 'В чем удалять?', reply_markup=admin_kb.button_case_admin3)


#dp.callback_query_handler(lambda y: y.data and y.data.startswith('dl_'))
async def delete_callback_run(call: types.CallbackQuery):
    global table
    table = call.data.replace("dl_", "")
    read = await mysql_db.sql_read2(call.data.replace("dl_", ""))
    result = await asyncio.gather(read)
    for i in result:
        for x in i:
            await call.message.answer_photo(x[0], f'Название:\n{x[1]}\nОписание:\n{x[2]}', parse_mode=types.ParseMode.HTML,
                                            reply_markup=InlineKeyboardMarkup().
                                            add(InlineKeyboardButton(f'Удалить {x[1]}', callback_data=f'del {x[1]}')))


#dp.callback_query_handler(lambda c: c.data and c.data.startswith('del '))
async def delete_callback_data(call: types.CallbackQuery):
    await mysql_db.sql_delete(table, call.data.replace('del ', ''))
    await call.answer(text=f'{call.data.replace("del ", "")} удалена.', show_alert=True)


#@dp.message_handler(Text(equals='Загрузить') state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи имя")


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введи описание")


#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Куда сохранить?', reply_markup=admin_kb.button_case_admin2)


#dp.callback_query_handler(lambda x: x.data and x.data.startswith('add_'))
async def load_callback_run(cbq: types.CallbackQuery, state: FSMContext):
    await mysql_db.sql_add_command(state, cbq.data.replace('add_', ''))
    await cbq.answer(text="Успешно сохранено", show_alert=True)
    await state.finish()


#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ОК')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, Text(equals='Загрузить'), state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(cm_delete, Text(equals='Удалить'))
    dp.register_message_handler(cm_show, Text(equals='Показать загруженное'))
    dp.register_callback_query_handler(load_callback_run, lambda x: x.data and x.data.startswith("add_"))
    dp.register_callback_query_handler(show_callback_run, lambda y: y.data and y.data.startswith('show_'))
    dp.register_callback_query_handler(delete_callback_run, lambda z: z.data and z.data.startswith("dl_"))
    dp.register_callback_query_handler(delete_callback_data, lambda c: c.data and c.data.startswith('del '))

