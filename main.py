import handlers
from loader import bot

handlers.start
handlers.help
handlers.story
handlers.weather
handlers.get_location
handlers.get_weather

if __name__ == '__main__':
    bot.infinity_polling()
