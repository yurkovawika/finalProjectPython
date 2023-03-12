import datetime
from abc import abstractmethod


class data_time():

    @abstractmethod
    def creat_data(self):
        c_data = datetime.date.today()
        res_data = str(c_data.strftime("%Y-%m-%d"))
        return ("{}".format(res_data))

    @abstractmethod
    def creat_time(self):
        c_time = datetime.datetime.now().time().strftime('%H:%M:%S')
        return str("{}".format(c_time))
