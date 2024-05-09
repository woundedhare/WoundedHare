from loader import bot
from funcs.parser import parser
from config_data.config import JOKE_URL
import time
import random
from config_data.config import STIKERS

@bot.message_handler(commands=['story'])
def send_story(message):
    """
    Функция-хендлер, выводящая пользователю шутку на английском языке, в ответ на его команду /story,
     через функцию-парсер
    Args: message(object) - объект вводимого сообщения
    """
    bot.send_message(message.chat.id, parser(JOKE_URL))
    bot.send_sticker(message.chat.id, random.choice(STIKERS))
    time.sleep(9)
    bot.send_message(message.chat.id, '..Введи любую команду или название города.')