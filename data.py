from date_for_now import date_now
import datetime
class data:
    def start(self):
        self.cal = {
            1 : {
                1 : "Биология",
                2 : "Биология",
                3 : "Химия",
                4 : "Оборона Украины"
            },
            2 : {
                1 : "Оборона Украины",
                2 : "Физра",
                3 : "Английский",
                4 : None
            },
            3 : {
                1 : "Математика",
                2 : "Всемирная история",
                2.5 : "Химия",
                3 : "Математика",
                4 : "Зарубежная литература"
            },
            4 : {
                1 : "История Украины",
                2 : "География",
                3 : "Английский",
                3.5 : "Физика",
                4 : "Физика"
            },
            5 : {
                1 : "Информатика",
                2 : "Украинский язык",
                3 : "Украинская литература",
                4 : None
            }
        }
        self.full_time = date_now().full_date_return()
        self.data = str(datetime.now().strftime("%d"))
    def para(self):
        return date_now().para_return(self.data, date_now().quest_return(date_now().time_return()), self.cal, self.full_time)
    def peremena(self):
        return date_now().perema_now_retuen(date_now().quest_return())
    def time(self):
        return date_now().time_return()
    def quest(self):
        return date_now().quest_return(date_now().time_return())
