from aiogram import types, Dispatcher
from bot_instanse import bot
async def secret_word1(message: types.Message):
    await message.reply('Добрый день! Поликлиника MIN приветсвует.\nЧто у вас болит?')
async def secret_word2(message: types.Message):    await message.reply('Ситуация часто встречаемая\nКак давно болит?')
async def secret_word3(message: types.Message):
    await message.reply('Вы занимались самолечением?')
async def secret_word4(message: types.Message):    await message.reply('Что вы принимали?')
async def secret_word5(message: types.Message):    await message.reply('Даа, часто их принимают.\n Вы пробовали чай с лимоном?')
async def secret_word6(message: types.Message):    await message.reply('Советую пропить его перед сном последующие 3 дня')
async def secret_word7(message: types.Message):    await message.reply('Особо и нет, главное не пейте холодное и отоспитесь!')
async def secret_word8(message: types.Message):    await message.reply('До свидания!')

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word1, lambda word: "здравствуйте" in word.text)
    dp.register_message_handler(secret_word2, lambda word: 'горло и голова' in word.text)
    dp.register_message_handler(secret_word3, lambda word: '3 дня' in word.text)
    dp.register_message_handler(secret_word4, lambda word: 'да' in word.text)
    dp.register_message_handler(secret_word5, lambda word: 'мукалтин и аспирин' in word.text)
    dp.register_message_handler(secret_word6, lambda word: 'нет еще' in word.text)
    dp.register_message_handler(secret_word7, lambda word: 'хорошо, есть еще что нужно принимать?' in word.text)
    dp.register_message_handler(secret_word8, lambda word: 'спасибо, всего доброго' in word.text)
