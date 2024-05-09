from telebot import types


all_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
help = types.KeyboardButton('/help')
story = types.KeyboardButton('/story')
weather_button = types.KeyboardButton('/weather')
all_keyboard.add(help, story, weather_button)
