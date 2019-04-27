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
            tmp = random_mess[randint(0, len(random_mess)-1)]
            bot.send_message(message.chat.id, tmp)
            if tmp[:10] == "Самый умны" :
                bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
            elif tmp[:10] == "729mxx5mcg" :
                bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))


    @bot.message_handler(commands=["help"])
    def cmd_help(message) :
        bot.send_message(message.chat.id, "Надо же! Раньше помощи у 'Вечера в хату' всегда просил, а теперь ко мне обращаешься. Вот иди к ним, и у них ищи помощи. После первого апреля они отправили уже достаточно того, что может тебе помочь.")


    @bot.message_handler(content_types=["text"])
    def all_messages(message) :
        currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow"))
        tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
        tmp_tmp = tmp.split()

        if message.text == "Now_time" : ##for search bags
            bot.send_message(message.chat.id, "current time: " + tmp)
            
        elif message.text.lower() == "красный треугольник" : #nom2
            if int(base.get_param(message.chat.id, 6)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 6)
                bot.send_message(message.chat.id, "Молодец! Знай же, тебе нужен восьмой том.")
            else :
                tmp = random_mess[randint(0, len(random_mess)-1)]
                bot.send_message(message.chat.id, tmp)
                if tmp[:10] == "Самый умны" :
                    bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
                elif tmp[:10] == "729mxx5mcg" :
                    bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))

        #nom3        
        elif message.text.lower() == "доброе утро" and int(base.get_param(message.chat.id, 2)) == 4 :
            if int(base.get_param(message.chat.id, 7)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 7)
                bot.send_message(message.chat.id, "Молодец, ты нашел ещё одну пасхалку. Надеюсь, это поможет тебе дальше. Полка номер 4")
            else :
                tmp = random_mess[randint(0, len(random_mess)-1)]
                bot.send_message(message.chat.id, tmp)
                if tmp[:10] == "Самый умны" :
                    bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
                elif tmp[:10] == "729mxx5mcg" :
                    bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))

        #nom4
        elif message.text == "IIPPRTRLVEYMPIL" :
            if int(base.get_param(message.chat.id, 8)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 8)
                bot.send_message(message.chat.id, "Какой же ты молодец! Держи еще подсказку. Стена 1.")
            else :
                tmp = random_mess[randint(0, len(random_mess)-1)]
                bot.send_message(message.chat.id, tmp)
                if tmp[:10] == "Самый умны" :
                    bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
                elif tmp[:10] == "729mxx5mcg" :
                    bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))


        #nom5
        elif message.text == "120" :
            if int(base.get_param(message.chat.id, 9)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 9)
                bot.send_message(message.chat.id, "Точно! Вот видишь, умение решать интегралы через Гамма-функцию тебе уже пригодилось в жизни! Ты получаешь дополнительный балл, но ответ тебе может еще пригодиться в дальнейшем. Запомни его")
            else :
                tmp = random_mess[randint(0, len(random_mess)-1)]
                bot.send_message(message.chat.id, tmp)
                if tmp[:10] == "Самый умны" :
                    bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
                elif tmp[:10] == "729mxx5mcg" :
                    bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))
                
        #this is the end
                #nom6
        elif message.text == "dfisfourty" :
            if int(base.get_param(message.chat.id, 10)) == 0 :
                base.plus_plus(message.chat.id, 3)
                base.trigger(message.chat.id, 10)
                bot.send_message(message.chat.id, "Браво! Поздравляю с прохождением онлайн части квеста ко дню физика. На самом ДФ тоже будут пасхалки. Стоит прийти пораньше, так как весь квест можно будет пройти только начав с утра. Дальнейшая информация, намекающая, где искать вход в кроличью нору появится в группе https://vk.com/df_msu. За прохождение онлайн-части полагается превелегия - в случае, если возникли проблемы с прохождением, всегда можно запросить подсказку здесь же.")
            else :
                tmp = random_mess[randint(0, len(random_mess)-1)]
                bot.send_message(message.chat.id, tmp)
                if tmp[:10] == "Самый умны" :
                    bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
                elif tmp[:10] == "729mxx5mcg" :
                    bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))

                
        elif int(tmp_tmp[0]) == 18 and message.text in ["1", "2", "3"] :
            if int(base.get_param(message.chat.id, 3)) >= int(message.text) :
                bot.send_message(message.chat.id, "Подсказка №" + str(message.text))
                #bot.send_photo(message.chat.id, open("help" + str(message.text) + ".png", "rb"))
                #check
                base.update(message.chat.id, 3, int(base.get_param(message.chat.id, 3)) - int(message.text))
                bot.send_message(message.chat.id, "На твоем счету " + base.get_param(message.chat.id, 3) + " coins")
            else :
                bot.send_message(message.chat.id, "Недостаточно средств.")
                bot.send_message(message.chat.id, "На твоем счету " + base.get_param(message.chat.id, 3) + " coins")
            
        
        else :
            tmp = random_mess[randint(0, len(random_mess)-1)]
            bot.send_message(message.chat.id, tmp)
            if tmp[:10] == "Самый умны" :
                bot.send_photo(message.chat.id, open("integral.jpg", "rb"))
            elif tmp[:10] == "729mxx5mcg" :
                bot.send_photo(message.chat.id, open("vavilon.jpg", "rb"))
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
                    if int(d) == 18 :
                        bot.send_message(us, "С днем физика!")
                        bot.send_message(us, "Ты славно потрудился за эти дни и имеешь на своем счету целых " + base.get_param(us, 3) + " coins. \nТеперь ты можешь купить на них подсказки, которые помогут тебе выиграть в квесте. \nВажно: В ответе на сообщения пришли только один номер желаемой подсказки.")
                        bot.send_message(us, "номер -- наименование, стоимость\n1 -- подсказка №1, 1 coins\n2 -- подсказка №2, 2 coins\n3 -- подсказка №3, 3 coins" )
                    else :
                        if int(base.get_param(us, 2)) == 3 :
                            bot.send_message(us, "<code>Доброе утро</code>" + ". До дня Физика осталось: " + str(remine_time) + "день",  parse_mode = "html")
                            #bot.send_message(us, "До дня Физика осталось: " + str(remine_time) + "день")
                        else :
                            bot.send_message(us, "Доброе утро! До дня Физика осталось: " + str(remine_time))
                    base.trigger(us, 4)
                    base.plus_plus(us, 2)
                time.sleep(1/5)
                    
        elif int(H) == 0 :
            for us in list(base.base.keys()) : ## триггер на ноль
                base.trigger(us, 4)

        time.sleep(300)
                    

        
def main() :
    threading.Thread(target = thread_spam).start()
    threading.Thread(target = thread_bot).start()
    

if __name__ == '__main__':  
    main()
