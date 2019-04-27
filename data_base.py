# -*- coding: utf-8 -*-

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

class Base :
    def __init__(self) :
        CREDENTIALS_FILE = 'df40bot-a3dfb58d30b4.json'
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
        self.spreadsheetId = '1L1mks111-PDHHfM3gPweTAh-7IdFFNqgLmub0ylpUyY'
        #self.sheet = self.service.spreadsheets().get(spreadsheetId = c)
        self.base = dict()
        self.cnt_user = 1 #0 #nomber of user in table
        self.params = {"0": "A", "1": "B", "2": "C", "3": "D",
                       "4": "E", "5": "F", "6": "G", "7": "H",
                       "8": "I", "9": "J", "10": "K"}


    def recovery(self) :
        values = self.service.spreadsheets().values().get(spreadsheetId = self.spreadsheetId, range = "A2:A10000").execute()["values"]
        self.base = dict()
        cnt = 1
        for el in values :
            cnt += 1
            self.base[str(el[0])] = cnt
        self.cnt_user = cnt


    def update(self, chat_id, cell, value) :
        self.service.spreadsheets().values().batchUpdate(spreadsheetId = self.spreadsheetId, body = {
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": "df40_bot!" + self.params[str(cell)] + str(self.base[str(chat_id)]),
                 "majorDimension": "ROWS",
                 "values": [[str(value)]]}
                ]
            }).execute()


    def more_update(self, chat_id, l_cell, r_cell, values) : #включительно в обе стороны
        for cell in range(l_cell, r_cell + 1) :
            Base.update(self, chat_id, cell, values[cell - l_cell])


    def get_param(self, chat_id, cell) :
        tmp_cell = self.params[str(cell)] + str(self.base[str(chat_id)])
        return self.service.spreadsheets().values().get(spreadsheetId = self.spreadsheetId, range = tmp_cell).execute()["values"][0][0]


    def get_params(self, chat_id, l_cell, r_cell) :
        tmp = []
        for cell in range(l_cell, r_cell + 1) :
            tmp.append(Base.get_param(self, chat_id, cell))
        return tmp
    
    
    def add_user(self, chat_id, username) :
        if self.base.get(str(chat_id)) is None :
            self.cnt_user += 1
            self.base[str(chat_id)] = self.cnt_user
            params = [chat_id, username, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            Base.more_update(self, chat_id, 0, len(params)-1, params)


    def trigger(self, chat_id, nomb_param) :
        tmp = int(Base.get_param(self, chat_id, nomb_param))
        tmp = abs(tmp - 1)
        Base.update(self, chat_id, nomb_param, tmp)


    def plus_plus(self, chat_id, nomb_param) :
        tmp = int(Base.get_param(self, chat_id, nomb_param))
        tmp += 1
        Base.update(self, chat_id, nomb_param, tmp)


    def pprint(self) :
        print(self.base, self.cnt_user)


if __name__ ==  "__main__" :
    a = Base()
    a.pprint()
    a.recovery()
    a.pprint()
##    a.plus_plus(260850155, 10)
##    a.trigger(260850155, 10)
##    print(a.get_params(260850155, 0, 10))
##    a.add_user(123, "lel")
##    a.pprint()
##    a.add_user(321, "")
##    a.pprint()
##    b = Base()
##    b.recovery()
##    b.pprint()
##    a.more_update(123, 1, 3, [12, "j", 3])
##    a.more_update(260850155, 5, 7, [1, 1])
##    a.update(321, 7, 1)
##    print(a.get_param(260850155, 1)
##    print(a.get_params(260850155, 0, 2))
##    print(a.trigger(260850155, 4))
##    a.plus_plus(260850155, 4)
    
