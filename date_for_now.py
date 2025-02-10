import datetime
import calendar

class date_now:
    def date_return(self):
        res = datetime.datetime.now()
        return int(res.weekday() + 1)
    def full_date_return(self):
        cogda_mounth, cogda_day = 2, 10
        mounth = int(datetime.datetime.now().strftime("%m"))
        day = int(datetime.datetime.now().strftime("%d"))
        now = 1
        for i in range(mounth - cogda_mounth + 1):
            for j in range(1, calendar.monthrange(2025, i + cogda_mounth)[1] + 1):
                if i == 0 and j <= 9:
                    pass
                else:
                    if self.date_for_weekly(cogda_mounth + i, j) == 1:
                        if now == 0:
                            now = 1
                        else:
                            now = 0
                    if i + cogda_mounth == mounth and j >= day:
                        break
        return now

    def date_for_weekly(self, mounth, day):
        date = datetime.date(2025, mounth, day)
        return date.isoweekday()

    def time_return(self):
        time = datetime.datetime.now().strftime("%H:%M")
        return time

    def quest_return(self):
        data = self.time_return().split(":")
        time = float(f"{data[0]}.{data[1]}")
        if time >= 8.0 and time <= 9.50:
            if time >= 8.0 and time <= 8.30:
                return -1
            else:
                return 1
        elif time >= 9.50 and time <= 11.20:
            if time >= 9.50 and time <= 11.0:
                return -2
            else:
                return 2
        elif time >= 11.20 and time <= 13.20:
            if time >= 11.20 and time <= 12.0:
                return -3
            else:
                return 3
        elif time >= 13.20 and time <= 14.50:
            if time >= 13.20 and time <= 13.30:
                return -4
            else:
                return 4
    def perema_now_retuen(self):
        if self.quest_return() < 0:
            return True
        else:
            return False
    def para_return(self):
        cal = {
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

        parameters = []
        quest = self.quest_return()
        data = self.date_return()

        if data <= 5:
            if quest < 0:
                parameters.append("Перемена")
            else:
                parameters.append("Урок")
            for i in range(1, 4 + 1):
                if quest == i or quest == i * -1:
                    if data != 3 and data != 4:
                        parameters.append(cal.get(data).get(i))
                    else:
                        if data == 3 and quest == 2 or quest == 2 * -1:
                            parameters.append(cal.get(data).get(2.5))
                        elif data == 4 and quest == 3 or quest == 3 * -1:
                            parameters.append(cal.get(data).get(3.5))
                        elif quest == i or quest == i * -1:
                            parameters.append(cal.get(data).get(i))

            return parameters
        else:
            return "Выходные"

if __name__ == '__main__':
    print(date_now().full_date_return())
