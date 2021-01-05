

# Импортируем необходимые компоненты
import logging
import os

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import Filters

from settings import TG_TOKEN
from handlers import *





#нкцию main, которая соединяется с платформой Telegram
def main():

    # описываем функцию (тело функции)
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN, use_context=True)
    
    PORT = int(os.environ.get('PORT', 5000))
    updater=Updater(TG_TOKEN,use_context=True)
    updater.start_webhook(listen="0.0.0.0",
    port=int(PORT),
    url_path=TG_TOKEN)
    updater.bot.setWebhook('https://surveyvegas.herokuapp.com/' + TG_TOKEN)



    logging.basicConfig(format='%(asctime)s-$(levelname)s-$(message)s',
                    level=logging.INFO,
                    filename='bot.log')

   
    
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик команды start
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('1|2|3|4|5|ЗАПОВНИТИ АНКЕТУ'),anketa_set_question))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('ЗАВЕРШИТИ ЗАПОВНЕННЯ'),thanks))
   
                  
    
    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
  

  

    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
