import requests
from keyboards.all_keyboard import all_keyboard
from loader import bot
from funcs.weather_id import weather_mode
import json
from config_data.config import API_KEY
import time
import sqlite3


@bot.message_handler(content_types=['location'])
def print_location(message):
    """
    Функция-хендлер, получающая на вход через декоратор местоположение пользователя и выводящее погоду по нему
    :param message: Message
    :return: None
    """

    if message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        user_id = message.from_user.id
        with sqlite3.connect('C:\PycharmProjects\python_basic_diplom\locations.db') as conn:
            cursor = conn.cursor()
            # Создаем таблицу, если она не существует
            cursor.execute('''CREATE TABLE IF NOT EXISTS locations 
                            (user_id INTEGER PRIMARY KEY, latitude REAL, longitude REAL)''')
            # Записываем пользователя в базу данных
            cursor.execute('''INSERT OR IGNORE INTO locations (user_id, latitude, longitude)
                              VALUES (?, ?, ?)''', (user_id, lat, lon))
            conn.commit()
        bot.send_message(message.chat.id, 'Ваша геолокация записана. Теперь по команде \weather вы будете получать погоду по ней.')
        req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric')

        if req.status_code == 200:
            data = json.loads(req.text)
            weather_id = data['weather'][0]['id']
            bot.send_message(message.chat.id,
                             f'Температура воздуха в вашем населённом пункте сейчас {round(data["main"]["temp"])} градусов.'
                             f' {weather_mode(weather_id)[0]}. Скорость ветра {data["wind"]["speed"]} м/с, влажность -'
                             f' {data["main"]["humidity"]} %.')
            bot.send_sticker(message.chat.id, weather_mode(weather_id)[1], reply_markup=all_keyboard)
            time.sleep(4)
            bot.send_message(message.chat.id, 'Введи любую команду или название города.')
        else:
            bot.send_message(message.chat.id, '<Запрос не прошёл>')
