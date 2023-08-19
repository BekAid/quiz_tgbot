from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton,InlineKeyboardMarkup
from bot_instanse import dp, bot
from parser import tv_show, phone_shop
from database import bot_db



# quiz v1
#quiz v1
async def quiz1(message: types.Message):
    question1 = "Зимой и летом одним цветом"
    answer = ['елка', "бабочка", "Дом", "Комп"]
    await bot.send_poll(message.chat.id,
                        question=question1,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation='Эх ты как ты не угадал детскую загадку',
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )

async def start_game(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_game_1 = InlineKeyboardButton('Next', callback_data='button_game_1')
    markup.add(button_game_1)
    question = "Что из этого не относится к основным физиологическим показателям?"
    answer = ["Цвет волос", "Температуратела", "Пульс"]
    image = open("media/физиология.jpg", 'rb')
    await bot.send_photo(message.chat.id, photo=image)
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )


async def game_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_2 = InlineKeyboardButton('Next', callback_data='button_game_2')
    markup.add(button_game_2)
    question = 'Сколько всего существует групп крови?'
    answer = ["3 (0, А, В)", "2 (0, А)", "4 (0, А, В, АВ)"]
    image = open("media/кровь.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_3 = InlineKeyboardButton('Next', callback_data='button_game_3')
    markup.add(button_game_3)
    question = 'Как называется прозрачная мембрана, которая проводит свет к сетчатке глаза?'
    answer = ["Хрусталик", "Ресница", "Роговица"]
    image = open("media/глаз.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_4 = InlineKeyboardButton('Next', callback_data='button_game_4')
    markup.add(button_game_4)
    question = 'Частота сердечных сокращений 60–80 ударов в минуту считается…'
    answer = ["Нормальной", "Пониженной", "Повышенной"]
    image = open("media/сердце.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )
async def game_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_5 = InlineKeyboardButton('Next', callback_data='button_game_5')
    markup.add(button_game_5)
    question = 'Сжигаем ли мы калории во время сна?'
    answer = ["Нет", "Да", "Зависит от массы тела"]
    image = open("media/калории.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_6 = InlineKeyboardButton('Next', callback_data='button_game_6')
    markup.add(button_game_6)
    question = 'Сколько в среднем живет человеческий волос?'
    answer = ["От 1 до 2 лет", "От 3 до 6 лет", "От 5 до 10 лет"]
    image = open("media/волос.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_7 = InlineKeyboardButton('Next', callback_data='button_game_7')
    markup.add(button_game_7)
    question = 'А теперь назови самую маленькую клетку в мужском организме'
    answer = ["Сперматозоид", "Астроцит", "Нейрон", "Эритроцит"]
    image = open("media/клетка.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_8 = InlineKeyboardButton('Next', callback_data='button_game_8')
    markup.add(button_game_8)
    question = 'Назови самую большую клетку в женском теле.'
    answer = ["Клетка молочной железы", "Нейрон", "Яйцеклетка", "Клетка Сертоли"]
    image = open("media/клеткажен.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_game_9 = InlineKeyboardButton('Next', callback_data='button_game_9')
    markup.add(button_game_9)
    question = 'Наиболее частой причиной смерти при сахарном диабете 1 типа является:'
    answer = ["Диабетическая нефропатия", "Инфаркт миокарда", "Кетоацидотическая кома", "Гангрена нижних конечностей",
              "Гиперосмолярная кома"]
    image = open("media/сахар.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        reply_markup=markup,
                        explanation='Ты точно в меде учишься?',
                        )

async def game_9(call: types.CallbackQuery):
    question = 'Сколько костей у человека?'
    answer = ['205-208', "100-105", "199-201"]
    image = open("media/кости.jpg", 'rb')
    await bot.send_photo(call.message.chat.id, photo=image)
    await bot.send_poll(call.message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        explanation='Ты точно в меде учишься?',
                        )

#for parser
async def parser_manas_film(message: types.Message):
    data = tv_show.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)
    #await bot.send_message(message.chat.id, data)

async def parser_kivano_phone(message: types.Message):
    data = phone_shop.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)
    #await bot.send_message(message.chat.id, data)

# Для вызова просмотра из бд результаты
async def show_min_command(message: types.Message):
    await bot_db.sql_command_select(message)


#Регистрация наших хендлеров квиз
def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=["quiz"])
    dp.register_message_handler(start_game, commands=['game'])
    dp.register_message_handler(parser_manas_film, commands=['parse_film'])
    dp.register_message_handler(parser_kivano_phone, commands=['parse_phone'])
    dp.register_message_handler(show_min_command, commands=['show_all'])

#Регистрация наших колбеков квиз
def register_quiz_call(dp: Dispatcher):
    dp.register_callback_query_handler(game_1, lambda func: func.data == 'button_game_1')
    dp.register_callback_query_handler(game_2, lambda func: func.data == 'button_game_2')
    dp.register_callback_query_handler(game_3, lambda func: func.data == 'button_game_3')
    dp.register_callback_query_handler(game_4, lambda func: func.data == 'button_game_4')
    dp.register_callback_query_handler(game_5, lambda func: func.data == 'button_game_5')
    dp.register_callback_query_handler(game_6, lambda func: func.data == 'button_game_6')
    dp.register_callback_query_handler(game_7, lambda func: func.data == 'button_game_7')
    dp.register_callback_query_handler(game_8, lambda func: func.data == 'button_game_8')
    dp.register_callback_query_handler(game_9, lambda func: func.data == 'button_game_9')