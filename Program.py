
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
                return Data.__month__index(i)
        else:
            return None

    def day(str):
        for i in Data.__week__:
            if i in str:
                if str[str.find(i) -3].isdigit():
                    return str[str.find(i) - 3 : str.find(i) - 1]
                else:
                    return str[str.find(i) - 2: str.find(i) - 1]
        return None
    # def day_week(str):




def without_data(str):
    __month__ = ["января", "февраля", "марта",  "апреля", "мая",  "июня",  "июля",  "августа", "сентября", "октября",  "ноября",  "декабря",]
    __week__ = ["понедельник", "вторник", "среду", "четверг", "пятницу", "субботу", "воскресенье"]
    for i in __month__:
        if i in str:
            if str[str.find(i) - 3].isdigit():
                return str[:str.find(i) - 3]
            else:
                return str[:str.find(i) - 2]

    for i in __week__:
        if i in str:
            return str[:str.find(i) - 3]

