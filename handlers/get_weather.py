import requests
from loader import bot
from funcs.weather_id import weather_mode
import json
from config_data.config import API_KEY
import random
import time


@bot.message_handler(content_types=['text'])
def get_weather(message):
    """
    Функция-хендлер, выводящая сообщение о погоде пользователю в ответ на введённое им название города
    Args: message(object) - объект вводимого сообщения
    """

    city = message.text.strip().lower()
    if len(city) > 25:
        bot.send_message(message.chat.id, 'Не понимаю вас, введите город, нажмите на кнопку или введите команду.')
    elif ('пасиб' in city) or ('благодар' in city):
        bot.send_message(message.chat.id, random.choice(['Всегда к вашим услугам.', 'Не стоит благодарности!', 'И вам спасибо.']))
        time.sleep(3)
        bot.send_message(message.chat.id, 'Введите город или команду.')
    elif ('привет' in city) or ('здорово' in city) or ('здравствуй' in city):
        bot.send_message(message.chat.id, random.choice(['Привет-привет!', 'Здравствуйте!']))
        time.sleep(3)
        bot.send_message(message.chat.id, 'Введите город или команду.')
    else:
        req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
        if req.status_code == 200:
            data = json.loads(req.text)
            weather_id = data['weather'][0]['id']
            bot.send_message(message.chat.id,
                             f'Температура воздуха в городе {message.text} сейчас {round(data["main"]["temp"])} градусов.'
                             f' {weather_mode(weather_id)[0]}. Скорость ветра {data["wind"]["speed"]} м/с, влажность -'
                             f' {data["main"]["humidity"]} %.')

            bot.send_sticker(message.chat.id, weather_mode(weather_id)[1])
        else:
            bot.reply_to(message, 'Город указан неверно.')
