from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_quiz = KeyboardButton("/quiz")
button_game = KeyboardButton("/game")
button_dice = KeyboardButton("dice")
button_parse_phone = KeyboardButton("/parse_phone")
button_location = KeyboardButton("Share Locations", request_location=True)
button_info = KeyboardButton('Call developer', request_contact=True)

keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)
keyboard_stat.add(button_game, button_quiz, button_dice,button_parse_phone,button_location, button_info)