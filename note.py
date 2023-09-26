import datetime

class MyNote:
    def __init__(self, text, date=None):
        self.__text = text
        if date is None:
            self.__time_last_update = datetime.datetime.now()
        else:
            self.__time_last_update = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")

    def update(self, text):
        self.__text = text
        self.__time_last_update = datetime.datetime.now()

    def get_text(self):
        return self.__text
    
    def get_time_last_update(self):
        return self.__time_last_update