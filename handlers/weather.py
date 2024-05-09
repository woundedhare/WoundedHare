from loader import bot
from keyboards.geo import geo_board
import time
import sqlite3
import requests
import json
from funcs.weather_id import weather_mode
from config_data.config import API_KEY
from keyboards.all_keyboard import all_keyboard


@bot.message_handler(commands=['weather'])
def get_location(message):
    """
    Функция-хендлер, запрашивающий местоположение через кнопку "Отправить местоположение"
    Args: message(object) - объект вводимого сообщения
    """
    with sqlite3.connect('C:\PycharmProjects\python_basic_diplom\locations.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS locations 
                                    (user_id INTEGER PRIMARY KEY, latitude REAL, longitude REAL)''')
        cursor.execute("""SELECT * FROM locations WHERE user_id == ?""", (message.from_user.id,))
        result = cursor.fetchone()
    if result:
        user_id, lat, lon = result
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric')

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
    else:
        bot.send_message(message.chat.id, 'Поделись местоположением.', reply_markup=geo_board)
        time.sleep(2)
        bot.send_message(message.chat.id, '..Нажми на кнопку или введи название города.')
