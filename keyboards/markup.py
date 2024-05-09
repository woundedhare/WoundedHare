from telebot import types


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
story = types.KeyboardButton('/story')
weather_button = types.KeyboardButton('/weather')
markup.add(story, weather_button)
