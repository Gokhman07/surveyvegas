import requests
from bs4 import BeautifulSoup
from utility import get_keyboard
from  telegram import  KeyboardButton, ReplyKeyboardMarkup, ParseMode, Location, Venue, InlineKeyboardMarkup
from  telegram.ext import ConversationHandler
from glob import glob
from telegram import ReplyKeyboardRemove
from  random import  choice
from emoji import  emojize
#from sqlitedb import  mdb, search_place, build_keyboard


from utility import SMILE, back_but
#from mysqldb import *

i=0

def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    smile =emojize(choice(SMILE),use_aliases=True)

    reply_keyboard = [['ЗАПОВНИТИ АНКЕТУ']]
    bot.message.reply_text((f'Здравствуйте шановний клієнте {bot.message.chat.first_name} 😊!\n Я бот який збирає враження клієнтів від послуг компанії Vegas  ! \n '
                         f'Компанія Vegas  турбується про комфорт своїх клієнтів {smile}!!!'),reply_markup=ReplyKeyboardMarkup( reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
  

def anketa_set_question(bot, update):  # временно сохраняем ответ
    global i
    reply_keyboard = [["1", "2", "3", "4", "5"]]  # создаем клавиатуру
    quetions=[ "Оцените, пожалуйста, качество обслуживания в нашей компании:","Работа консультантов компании:",
    "Качество сервиса службы доставки:","Качество продукции:","Порекомендуете ли нас:"]   
    #quetions=get_questions()
   

    print(len(quetions))
   
    if i!=len(quetions):
        bot.message.reply_text(quetions[i],reply_markup=ReplyKeyboardMarkup( reply_keyboard, resize_keyboard=True, one_time_keyboard=True))  
        i=i+1
        print(i)
        
    else:
        reply_keyboard = [['ЗАВЕРШИТИ ЗАПОВНЕННЯ']]
        bot.message.reply_text("Коментарі до оцінки (напішіть або натисніть 'ЗАВЕРШИТИ ЗАПОВНЕННЯ')", reply_markup=ReplyKeyboardMarkup( reply_keyboard, resize_keyboard=True, one_time_keyboard=True))
        i=0
           
    
        # при нажатии клавиатура исчезает
    #return "evaluation"  # ключ для определения следующего шага

def thanks(bot, update):
    bot.message.reply_text("Дякуємо за Ваш відгук!!",reply_markup=ReplyKeyboardRemove())
  
def next_step():
    return "next"
def main_keyboard(bot, update):
    
  
    bot.message.reply_text("Главное меню", reply_markup=get_keyboard())

# функция печатает и отвечает на полученные геоданные
def get_location(bot, update):
    print('Hi')
    print(bot.message.location)
   # bot.message.reply_text('{}, мы получили ваше местоположение!'.format(bot.message.chat.first_name))

def make_keyboard(bot,update):
   result=[]
   result= build_keyboard(bot,update)

    
   reply_keyboard = []
   reply_keyboard.append("🔙")
   for el in result:
       print(el)
       reply_keyboard.append(el)
    
   
   

   # создаем клавиатуру
   bot.message.reply_text(
        f"{bot.message.text}",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard , resize_keyboard=True))

def sendPlace(bot, update):
   
    place = search_place( bot.message.text)
    print(place)
     
   
    bot.message.reply_text(place[8])
    if(place[7]):
       bot.message.reply_text(f"Сайт: {place[7]}")
    update.bot.send_venue(chat_id=bot.message.chat.id,latitude=place[3], longitude=place[4], title=place[1],address=place[2])

 
   
  
  

def parrot(bot, update):
    bot.message.reply_text(bot.message.text)














