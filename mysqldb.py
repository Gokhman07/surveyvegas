import mysql.connector



from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton



mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="printer10",
  database='oprosnik_for_vegas'


)
cursor = mydb.cursor()


# функция создает клавиатуру и ее разметку
def get_questions():

    cursor.execute("SELECT text FROM  questions")
    data= (cursor.fetchall())
    print(data)
    ls=[]
    for d in data:
      ls.append(d[0])
    print(ls)

    
  

 
    return ls

def get_url(name):
    cursor.execute(f"SELECT URL, conf_id, password  FROM  TEACHERS WHERE Name ='{name}'")
    data= list(cursor.fetchall())
   
    
    conf=[]
    for col in data[0]:
      if col != None:
        conf.append(col)

    print(conf)
    return conf


    
