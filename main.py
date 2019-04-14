# -*- coding: utf-8 -*-


import const
import telebot
import threading
import data_base
import pytz
import time
from datetime import datetime
from random import randint

def thread_bot() :
    token = const.token
    bot = telebot.TeleBot(token)
    base = data_base.Base()
    base.recovery()
    random_mess = const.random_mess
    
    @bot.message_handler(commands=["start"])
    def cmd_start(message) :
        base.add_user(message.chat.id, message.from_user.username)
        if int(base.get_param(message.chat.id, 5)) == 0 :
            bot.send_message(message.chat.id, "У тебя что-то есть для меня?")
            base.trigger(message.chat.id, 5)
            base.plus_plus(message.chat.id, 3)
        else :
            bot.send_message(message.chat.id, random_mess[randint(0, len(random_mess)-1)])

    @bot.message_handler(content_types=["text"])
    def all_messages(message) :
        currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow"))
        tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
        tmp_tmp = tmp.split()

        if message.text == "Now_time" : ##for search bags
            bot.send_message(message.chat.id, "current time: " + tmp)
            
        elif message.text == "text from p.2" : #nom2
            if int(base.get_param(message.chat.id, 6)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 6)
                bot.send_message(message.chat.id, "Поздравляем, вы нашли вторую пасхалку.")
            else :
                bot.send_message(message.chat.id, random_mess[randint(0, len(random_mess)-1)])

        #nom3        
        elif message.text.lower() == "доброе утро" and int(base.get_param(message.chat.id, 2)) == 4 :
            if int(base.get_param(message.chat.id, 7)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 7)
                bot.send_message(message.chat.id, "Поздравляем, вы нашли третью пасхалку.")
            else :
                bot.send_message(message.chat.id, random_mess[randint(0, len(random_mess)-1)])
                
        elif int(tmp_tmp[0]) == 19 and message.text in ["1", "2", "3"] :
            if int(base.get_param(message.chat.id, 3)) >= int(message.text) :
                bot.send_message(message.chat.id, "Подсказка №" + str(message.text))
                #bot.send_photo(message.chat.id, open("help" + str(message.text) + ".png", "rb"))
                base.update_param(message.chat.id, 3, int(base.get_param(message.chat.id, 3)) - int(message.text))
                bot.send_message(message.chat.id, "На твоем счету " + base.get_param(message.chat.id, 3) + " coins")
            else :
                bot.send_message(message.chat.id, "Недостаточно средств.")
                bot.send_message(message.chat.id, "На твоем счету " + base.get_param(message.chat.id, 3) + " coins")
            
        
        else :
            bot.send_message(message.chat.id, random_mess[randint(0, len(random_mess)-1)])
            time.sleep(1/10)
            
    bot.polling(none_stop=True)


def thread_spam() :
    token = const.token
    bot = telebot.TeleBot(token)
    base = data_base.Base()
    base.recovery()
    while True :
        base = data_base.Base()
        base.recovery()
        currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow"))
        tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
        d, m, Y, H, M, S = tmp.split()
        remine_time = datetime(2019, 5, 18) - datetime(int(Y), int(m), int(d))
        remine_time = int(str(remine_time).split()[0])
        if int(H) == 8 :
            for us in list(base.base.keys()) :
                if int(base.get_param(us, 4)) == 0 :
                    if int(d) == 19 :
                        bot.send_message(us, "С днем физика!")
                        bot.send_message(us, "Ты славно потрудился за эти дни и имеешь на своем счету целых " + base.get_param(us, 3) + " coins. \nТеперь ты можешь купить на них подсказки, которые помогут тебе выиграть в квесте. \nВажно: В ответе на сообщения пришли только один номер желаемой подсказки.")
                        bot.send_message(us, "номер -- наименование, стоимость\n1 -- подсказка №1, 1 coins\n2 -- подсказка №2, 2 coins\n3 -- подсказка №3, 3 coins" )
                    else :
                        if int(base.get_param(us, 2)) == 3 :
                            bot.send_message(us, "<code>Доброе утро</code>",  parse_mode = "html")
                            bot.send_message(us, "До дня Физика осталось: " + str(remine_time))
                        else :
                            bot.send_message(us, "Доброе утро! До дня Физика осталось: " + str(remine_time))
                    base.trigger(us, 4)
                    base.plus_plus(us, 2)
                time.sleep(1/5)
                    
        elif int(H) == 0 :
            for us in list(base.base.keys()) :
                base.trigger(us, 4)

        time.sleep(300)
                    

        
def main() :
    threading.Thread(target = thread_spam).start()
    threading.Thread(target = thread_bot).start()
    

if __name__ == '__main__':  
    main()
