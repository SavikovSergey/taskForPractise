import datetime
from datetime import datetime

now = datetime.now()
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
current_datetime = datetime.now()

class Data:
    __month__ = ["января", "февраля", "марта",  "апреля", "мая",  "июня",  "июля",  "августа", "сентября", "октября",  "ноября",  "декабря",  ]
    __week__ = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    def year(str):
        text = ["года"]
        for i in text:
            if i in str:
                return str[str.find(i) - 5:str.find(i)-1]
        else:
            return None

    def month(str):
        for i in Data.__month__:
            if i in str:
                return Data.__month__.index(i) + 1
        else:
            return None

    def day(str):
        for i in Data.__month__:
            if i in str:
                if str[str.find(i) -3].isdigit():
                    return str[str.find(i) - 3 : str.find(i) - 1]
                else:
                    return str[str.find(i) - 2: str.find(i) - 1]
        return None
    def time(str):
        global MESSAGE
        if str.rfind(":") and str[str.rfind(":")-1].isdigit() and str[str.rfind(":")+1].isdigit():
            time = str[str.rfind(":") - 2:str.rfind(':') + 3]
            if time[0] == " ":
                MESSAGE['DATE']['hour'] = time[1:2]
                MESSAGE['DATE']['minute'] = time[3:]
            else:
                MESSAGE['DATE']['hour'] = time[:2]
                MESSAGE['DATE']['minute'] = time[3:]

        if ":" not in string:
            global now
            now = datetime.now()
            MESSAGE['DATE']['hour'] = current_hour
            MESSAGE['DATE']['minute'] = current_minute

def Text(str):
    __month__ = ["января", "февраля", "марта",  "апреля", "мая",  "июня",  "июля",  "августа", "сентября", "октября",  "ноября",  "декабря"]
    __week__ = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    __Time__ = [":"]

    for i in __week__:
        if i in str:
            return str[:str.find(i) - 3]

    for i in __month__:
        if i in str:
            return str[:str.find(i) - 3]

    for i in __Time__:
        if i in str:
            return str[:str.find(i) - 5]

    else:
        return str[:]

try:
    string = input()
    MESSAGE = {'STATUS': None,'TEXT': None, 'DATE': {'year': None, 'month': None, 'day': None, 'day_of_week': None, 'hour': None, 'minute': None}}
    if "понедельник" not in string or "вторник" not in string or "среду" not in string or "четверг" not in string or "пятницу" not in string or "субботу" not in string or "воскресенье":
        MESSAGE['DATE']['day_of_week'] = current_datetime.weekday() + 1
        if current_datetime.weekday()+1 == 1:
            MESSAGE['DATE']['day_of_week'] = "Понедельник"
        elif current_datetime.weekday()+1 == 2:
            MESSAGE['DATE']['day_of_week'] = "Вторник"
        elif current_datetime.weekday()+1 == 3:
            MESSAGE['DATE']['day_of_week'] = "Среда"
        elif current_datetime.weekday()+1 == 4:
            MESSAGE['DATE']['day_of_week'] = "Четверг"
        elif current_datetime.weekday()+1 == 5:
            MESSAGE['DATE']['day_of_week'] = "Пятница"
        elif current_datetime.weekday()+1 == 6:
            MESSAGE['DATE']['day_of_week'] = "Суббота"
        elif current_datetime.weekday()+1 == 7:
            MESSAGE['DATE']['day_of_week'] = "Воскресенье"

    if "понедельник" in string:
        MESSAGE['DATE']['day_of_week'] = "Понедельник"
        Data.time(string)
    elif "вторник" in string:
        MESSAGE['DATE']['day_of_week'] = "Вторник"
        Data.time(string)
    elif "среду" in string:
        MESSAGE['DATE']['day_of_week'] = "Среда"
        Data.time(string)
    elif "четверг" in string:
        MESSAGE['DATE']['day_of_week'] = "Четверг"
        Data.time(string)
    elif "пятницу" in string:
        MESSAGE['DATE']['day_of_week'] = "Пятница"
        Data.time(string)
    elif "субботу" in string:
        MESSAGE['DATE']['day_of_week'] = "Суббота"
        Data.time(string)
    elif "воскресенье" in string:
        MESSAGE['DATE']['day_of_week'] = "Воскресенье"
        Data.time(string)
    else:
        MESSAGE['DATE']['year'] = Data.year(string)
        MESSAGE['DATE']['month'] = Data.month(string)
        MESSAGE['DATE']['day'] = Data.day(string)
        Data.time(string)
    MESSAGE['TEXT'] = Text(string)
    MESSAGE['STATUS'] = 'SUCCESS'
    MESSAGE['DATE']['year'] = Data.year(string)
    MESSAGE['DATE']['month'] = Data.month(string)
    MESSAGE['DATE']['day'] = Data.day(string)
    print(MESSAGE)
except Exception as e:
    MESSAGE['STATUS'] = 'ERROR'
    MESSAGE['TEXT'] = e
    print(MESSAGE)