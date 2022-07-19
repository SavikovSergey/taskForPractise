import datetime
from datetime import datetime, timedelta
from datetime import date

now = datetime.now()
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")
current_datetime = datetime.now()
current_year = now.strftime("%Y")
current_month = now.strftime("%B")
current_day = now.strftime("%a")
current_HandM = now.strftime("%H,%M")

class Data:
    __month__ = ["января", "февраля", "марта",  "апреля", "мая",  "июня",  "июля",  "августа", "сентября",
                 "октября",  "ноября",  "декабря",]
    __week__ = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    def year(str):
        text = ["года", "году"]
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
    __month__ = ["января", "февраля", "марта",  "апреля", "мая",  "июня",  "июля",  "августа", "сентября",
                 "октября",  "ноября",  "декабря"]
    __week__ = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    __Time__ = [":"]
    __year__ = ["году"]
    __day__ = ["завтра", "послезавтра"]
    __through__ = ["через"]

    for i in __week__:
        if i in str:
            return str[:str.find(i) - 3]

    for i in __month__:
        if i in str:
            return str[:str.find(i) - 3]

    for i in __Time__:
        if i in str:
            return str[:str.find(i) - 5]
    for i in __year__:
        if i in str:
            return str[:str.find(i) - 8]
    for i in __day__:
        if i in str:
            return str[:str.find(i) - 1]
    for i in __through__:
        if i in str:
            return str[:str.find(i) - 1]
    else:
        MESSAGE['DATE']['day_of_week'] = current_datetime.weekday() + 1
        if current_datetime.weekday() + 1 == 1:
            MESSAGE['DATE']['day_of_week'] = "Понедельник"
        elif current_datetime.weekday() + 1 == 2:
            MESSAGE['DATE']['day_of_week'] = "Вторник"
        elif current_datetime.weekday() + 1 == 3:
            MESSAGE['DATE']['day_of_week'] = "Среда"
        elif current_datetime.weekday() + 1 == 4:
            MESSAGE['DATE']['day_of_week'] = "Четверг"
        elif current_datetime.weekday() + 1 == 5:
            MESSAGE['DATE']['day_of_week'] = "Пятница"
        elif current_datetime.weekday() + 1 == 6:
            MESSAGE['DATE']['day_of_week'] = "Суббота"
        elif current_datetime.weekday() + 1 == 7:
            MESSAGE['DATE']['day_of_week'] = "Воскресенье"
        return str[:]

def through(list):
    global now
    if len(list)==1:
        if list[0] == "год":
            now += timedelta(days=365)
        elif list[0] == "месяц":
            now += timedelta(days=31)
        elif list[0] == "неделю":
            now += timedelta(days=7)
        elif list[0] == "день":
            now += timedelta(days=1)
        elif list[0] == "сутки":
            now += timedelta(hours=24)
        elif list[0] == "час":
            now += timedelta(hours=1)
        elif list[0] == "минуту":
            now += timedelta(minutes=1)
    elif list[1] == "года":
        now += timedelta(days=int(list[0]) * 365)
    elif list[1] == "лет":
        now += timedelta(days=int(list[0]) * 365)
    elif list[1] == "месяца":
        now += timedelta(days=int(list[0]) * 31)
    elif list[1] == "месяцев":
        now += timedelta(days=int(list[0]) * 31)
    elif list[1] == "недели":
        now += timedelta(days=int(list[0]) * 7)
    elif list[1] == "недель":
        now += timedelta(days=int(list[0]) * 7)
    elif list[1] == "дней":
        now += timedelta(days=int(list[0]))
    elif list[1] == "дня":
        now += timedelta(days=int(list[0]))
    elif list[1] == "суток":
        now += timedelta(days=int(list[0]))
    elif list[1] == "часов":
        now += timedelta(hours=int(list[0]))
    elif list[1] == "часа":
        now += timedelta(hours=int(list[0]))
    elif list[1] == "минут":
        now += timedelta(minutes=int(list[0]))
    elif list[1] == "минуты":
        now += timedelta(minutes=int(list[0]))

def timeforthrough(argnow):
    MESSAGE['DATE']['year'] = argnow.year
    MESSAGE['DATE']['month'] = argnow.month
    MESSAGE['DATE']['day'] = argnow.day
    MESSAGE['DATE']['hour'] = argnow.hour
    MESSAGE['DATE']['minute'] = argnow.minute
try:
    string = input()
    MESSAGE = {'STATUS': None,'TEXT': None, 'DATE': {'year': None, 'month': None, 'day': None}}
                                                     #'hour': None, 'minute': None}}

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

    if "завтра" in string:
        MESSAGE['DATE']['day_of_week'] = current_datetime.weekday() + 1
        if current_datetime.weekday() + 1 == 1:
            MESSAGE['DATE']['day_of_week'] = "Вторник"
        elif current_datetime.weekday() + 1 == 2:
            MESSAGE['DATE']['day_of_week'] = "Среда"
        elif current_datetime.weekday() + 1 == 3:
            MESSAGE['DATE']['day_of_week'] = "Четверг"
        elif current_datetime.weekday() + 1 == 4:
            MESSAGE['DATE']['day_of_week'] = "Пятница"
        elif current_datetime.weekday() + 1 == 5:
            MESSAGE['DATE']['day_of_week'] = "Суббота"
        elif current_datetime.weekday() + 1 == 6:
            MESSAGE['DATE']['day_of_week'] = "Воскресенье"
        else:
            MESSAGE['DATE']['day_of_week'] = "Понедельник"
    if "послезавтра" in string:
        MESSAGE['DATE']['day_of_week'] = current_datetime.weekday() + 1
        if current_datetime.weekday() + 1 == 1:
            MESSAGE['DATE']['day_of_week'] = "Cреда"
        elif current_datetime.weekday() + 1 == 2:
            MESSAGE['DATE']['day_of_week'] = "Четверг"
        elif current_datetime.weekday() + 1 == 3:
            MESSAGE['DATE']['day_of_week'] = "Пятница"
        elif current_datetime.weekday() + 1 == 4:
            MESSAGE['DATE']['day_of_week'] = "Суббота"
        elif current_datetime.weekday() + 1 == 5:
            MESSAGE['DATE']['day_of_week'] = "Воскресенье"
        elif current_datetime.weekday() + 1 == 6:
            MESSAGE['DATE']['day_of_week'] = "Понедельник"
        else:
            MESSAGE['DATE']['day_of_week'] = "Вторник"

    MESSAGE['TEXT'] = Text(string)
    MESSAGE['STATUS'] = 'SUCCESS'
    MESSAGE['DATE']['year'] = Data.year(string)
    MESSAGE['DATE']['month'] = Data.month(string)
    MESSAGE['DATE']['day'] = Data.day(string)
    if "послезавтра" in string:
        now += timedelta(days=2)
        MESSAGE['DATE']['day'] = now.strftime("%d")
    elif "завтра" in string:
        now += timedelta(days=1)
        MESSAGE['DATE']['day'] = now.strftime("%d")

    if "через" in string:
        str = string[string.rfind("через") + 6:]
        list = str.split(" ")
        now = datetime.now()
        while list:
            through(list[:2])
            list.remove(list[0])
        timeforthrough(now)

    if not MESSAGE['DATE']['year']:
        MESSAGE['DATE']['year'] = datetime.now().year
    if not MESSAGE['DATE']['month']:
        MESSAGE['DATE']['month'] = datetime.now().month
    if not MESSAGE['DATE']['day']:
        MESSAGE['DATE']['day'] = datetime.now().day
    print(MESSAGE)
except Exception as e:
    MESSAGE['STATUS'] = 'ERROR'
    MESSAGE['TEXT'] = e
    print(MESSAGE)