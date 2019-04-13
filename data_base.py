# -*- coding: utf-8 -*-
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Base :
    def __init__(self) :
        ## open table
        CREDENTIALS_FILE = "df40bot-e2824e1f5787.json"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',                                                                            'https://www.googleapis.com/auth/drive'])
        client = gspread.authorize(credentials)
        self.sheet = client.open('df40bot').sheet1
        
        self.base = dict()
        self.cnt_user = 1 #0
        self.params = {0: "chat_id", 1: "username", 2: "cnt_day",
                       3: "coins", 4: "flg_hello", 5: "flg_nom1",
                       6: "flg_nom2", 7: "flg_nom3"}

        
    def recovery(self) : ## user_id не начинается с нуля?
        request = self.sheet.get_all_records()
        cnt = 1
        for row in request :
            cnt += 1
            self.base[row["chat_id"]] = cnt
        self.cnt_user = cnt


    def add_user(self, chat_id, username) :
        if self.base.get(chat_id) is None :
            self.cnt_user += 1
            self.base[chat_id] = self.cnt_user
            row = [chat_id, username, 0, 0, 0, 0, 0, 0]
            self.sheet.insert_row(row, self.cnt_user)


    def get_row(self, chat_id) :
        return self.sheet.row_values(self.base[chat_id])


    def get_param(self, chat_id, nomber_param) :
        row = Base.get_row(self, chat_id)
        #print(row, "row")
        return row[nomber_param]


    def update_param(self, chat_id, nomber_param, new_value) :
        nomber_row = self.base[chat_id]
        self.sheet.update_cell(nomber_row, nomber_param + 1, new_value)


    def trigger(self, chat_id, nomber_param) :
        tmp = int(Base.get_param(self, chat_id, nomber_param))
        tmp = abs(tmp - 1)
        Base.update_param(self, chat_id, nomber_param, tmp)

    def plus_plus(self, chat_id, nomber_param) :
        tmp = int(Base.get_param(self, chat_id, nomber_param))
        tmp += 1
        Base.update_param(self, chat_id, nomber_param, tmp)


if __name__ == "__main__" :
##    a = Base()
##    a.recovery()
##    print(a.get_param(260850155, 5))
##    a.trigger(260850155, 5)
##    a.plus_plus(260850155, 3)
##    print(a.get_param(260850155, 5))
    import pytz
    from datetime import datetime
    import time
    currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow")).today()
    tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
    print(tmp)
    while True :
        currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow")).today()
        tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
        print(tmp)
        time.sleep(61)
        currernt_datatime = datetime.now(pytz.timezone("Europe/Moscow")).today()
        tmp = currernt_datatime.strftime("%d %m %Y %H %M %S")
        print(tmp)
