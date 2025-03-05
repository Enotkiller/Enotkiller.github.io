from aiogram.types import Message

from date_for_now import date_now
import datetime

class data:
    def start(self):
        self.cal = {
            1 : {
                1 : "Биология",
                1.5 : None,
                2 : "Биология",
                2.5 : None,
                3 : "Химия",
                3.5 : None,
                4 : "Оборона Украины",
                4.5 : None
            },
            2 : {
                1 : "Оборона Украины",
                1.5 : None,
                2 : "Физра",
                2.5 : None,
                3 : "Английский",
                3.5 : None,
                4 : None,
                4.5 : None
            },
            3 : {
                1 : "Математика",
                1.5 : None,
                2 : "Всемирная история",
                2.5 : "Химия",
                3 : "Математика",
                3.5 : "Зарубежная литература",
                4 : None,
                4.5 : None
            },
            4 : {
                1 : "История Украины",
                1.5 : None,
                2 : "География",
                2.5 : None,
                3 : "Английский",
                3.5 : "Физика",
                4 : "Физика",
                4.5 : None
            },
            5 : {
                1 : "Информатика",
                1.5 : None,
                2 : "Украинский язык",
                2.5 : None,
                3 : "Украинская литература",
                3.5 : None,
                4 : None,
                4.5 : None
            }
        }
        #все числа которые дробные это то что в знаменатиили на той паре то есть с начало идёт словвари от 1 до 5 - это дни нидели, а в них пары от 1 до 4, и если есть напимер что во вторик на второй паре если числитель то будет манеша, а если знаменатель то пишите 2.5 : инфа и когда будет знаменатель то напишет инфу а не матишу.
        self.url = {
            "Биология" : "https://meet.google.com/eed-rtog-srd",
            "Химия" : "https://meet.google.com/cut-rvao-zbt",
            "Оборона Украины" : "https://meet.google.com/uqv-omtr-bwx",
            "Физра" : "https://meet.google.com/mxt-wvmr-gny",
            "Английский" : "1 Группа: https://meet.google.com/svs-snwo-tfm\n2 Группа: https://meet.google.com/hdq-zamk-pka",
            "Математика" : "https://us02web.zoom.us/j/84351065107?pwd=WOrdR7On7gbcrPynf178H0A9FW3M3k.1",
            "Зарубежная литература" : "https://meet.google.com/mnx-uxwk-wgo",
            "История Украины" : "https://meet.google.com/zww-totu-kva",
            "География" : "https://meet.google.com/gyc-nwne-nvi",
            "Физика" : "https://meet.google.com/znu-moir-atb",
            "Информатика" : "https://meet.google.com/kwt-xdbj-kdq",
            "Украинский язык" : "https://meet.google.com/jkz-wqku-xyh",
            "Украинская литература" : "https://meet.google.com/nem-mhnk-ghe",
            "Всемирная история" : "https://meet.google.com/qay-vxca-jfw"
        }
        self.data =lambda : int(datetime.datetime.now().strftime("%d"))
        self.otmena_mass = [0, 0, 1, 0]
        self.x = 2
        # это на сколько увиличивается время, то есть если у вас 2 часа дня а x тоже 2 то тогда скажет что сейчас 4 часа дня, это надо для того что бы когда бот находится не в украине а в калифорнии как у меня, но так как в калифорнии на 2 часа меньше чем в укр, то время надо увиличить на 2.
        self.now = 1
        self.now_day = 10
        self.now_mounth = 2
        # пишите дату в now_day и now_mounth, а в now пишите какой тип недели в ту дату которую вы записали. 1 = числитель, 0 = знаменатель.
        self.id = []
        self.all = []
        self.username = []
    def read_file(self):
        self.all = []
        self.id = []
        self.username = []
        with open("ping.txt", "r") as file:
            for i in file.read().split("\n"):
                if i != '':
                    print(i)
                    self.all.append(i.split(" "))
                    self.id.append(i.split(" ")[0])
                    self.username.append(i.split(" ")[1])
    def ping(self, message : Message):
        self.read_file()

        if not str(message.from_user.id) in self.id:
            with open("ping.txt", "a") as file:
                if len(self.all) > 0:
                    file.write(f"\n{message.from_user.id} {message.from_user.username}")
                else:
                    file.write(f"{message.from_user.id} {message.from_user.username}")

        else:
            with open("ping.txt", "w"):
                pass
            mass = self.all
            self.all = []
            self.id = []
            self.username = []
            for i in mass:
                q = []
                for j in i:
                    if j == str(message.from_user.id) or j == str(message.from_user.username):
                        break
                    else:
                        q.append(j)
                if q != []:
                    with open("ping.txt", "a") as f:
                        f.write(f"{"\n"if len(self.all) != 0 else ""}{q[0]} {q[1]}")
                    self.username.append(q[1])
                    self.id.append(q[0])
                    self.all.append(q)
    def get_url(self):
        return self.url.get(self.para())
    def reverse_otmena(self):
        self.otmena_mass[2] = 2
        if (self.quest() if self.quest() > 0 else self.quest() * -1) > self.otmena_mass[1] or date_now().date_return() != self.otmena_mass[3]:
            self.otmena_mass[0] = 0
            self.otmena_mass[1] = 0
            self.otmena_mass[2] = 0
        else:
            self.otmena_mass[2] = 0
    def otmena_now(self):
        self.quest()
        return self.otmena_mass[0]
    def otmena(self):
        self.otmena_mass = [1, self.quest() if self.quest() > 0 else self.quest() * -1, 0, date_now().date_return()]
    def data_weekly(self):
        return date_now().date_return()
    def para(self, now_p = None):
        if now_p != None:
            now = now_p
        else:
            now = date_now().quest_return(date_now().time_return())
        return date_now().para_return(self.data_weekly(), now, self.cal, date_now().full_date_return(self.now, self.now_day, self.now_mounth))
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
    db.read_file()
    print(db.all)
    print(db.id)
    print(db.username)
