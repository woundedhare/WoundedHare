from telebot import types


geo_board = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
geo_button = types.KeyboardButton(text='Отправить местоположение', request_location=True)
geo_board.add(geo_button)
