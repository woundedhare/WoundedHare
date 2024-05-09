from telebot import types


markup_help = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markup_help.add(types.KeyboardButton('/help'))
