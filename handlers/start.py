from loader import bot
from keyboards.help import markup_help


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Функция-хендлер, выводящая приветствие и подсказки пользователю, в ответ на его команду /start
    Args: message(object) - объект вводимого сообщения
    """
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет, {name}! Я бот, выдающий погоду. А ещё я присылаю английские анекдоты.\n'
                                      f'/help - для получения функционала\n\n Введи название города.',
                     reply_markup=markup_help)
