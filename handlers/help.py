from loader import bot
from keyboards.markup import markup


@bot.message_handler(commands=['help'])
def help_welcome(message):
    """
    Функция-хендлер, выводящая сведения о командах бота пользователю, в ответ на его команду /help
    Args: message(object) - объект вводимого сообщения
    """
    bot.send_message(message.chat.id, 'Устроен я пока просто: ты вводишь название города, я - присылаю погоду.\n'
                                      '/story - английский анекдот\n'
                                      '/weather - погода по геолокации. Или просто введи название города.',
                     reply_markup=markup)
