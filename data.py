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
                3.5 : "Зарубежная литература"
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
        self.data = int(datetime.datetime.now().strftime("%d"))
        self.otmena_mass = [0, 0, 1]
    def reverse_otmena(self):
        self.otmena_mass[2] = 2
        if (self.quest() if self.quest() > 0 else self.quest() * -1) > self.otmena_mass[1]:
            self.otmena_mass[0] = 0
            self.otmena_mass[2] = 0
        else:
            self.otmena_mass[2] = 0

    def otmena_now(self):
        self.quest()
        return self.otmena_mass[0]
    def otmena(self):
        self.otmena_mass = [1, self.quest() if self.quest() > 0 else self.quest() * -1, 0]
    def data_weekly(self):
        return date_now().date_return()
    def data(self):
        self.data = int(datetime.datetime.now().strftime("%d"))
        return self.data
    def para(self):
        return date_now().para_return(self.data_weekly(), date_now().quest_return(date_now().time_return()), self.cal, self.full_time)
    def peremena(self):
        return date_now().perema_now_retuen(date_now().quest_return(date_now().time_return()))
    def time(self):
        return date_now().time_return()
    def quest(self):
        if self.otmena_mass[2] == 0:
            self.reverse_otmena()
        return date_now().quest_return(date_now().time_return())
    def time_float(self):
        return float(f"{date_now().time_return().split(":")[0]}.{date_now().time_return().split(":")[1]}")
if __name__ == '__main__':
    db = data()
    db.start()
    print(db.para())
    print(db.otmena_mass)
    db.otmena()
    print(db.otmena_mass)
    print(db.otmena_now())
    print(db.otmena_mass)
    print(db.otmena_mass)