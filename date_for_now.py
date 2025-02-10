import datetime


class date_now:
    def date_return(self):
        res = datetime.datetime.now()
        return int(res.weekday() + 1)

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
                if (quest == i or quest == i * -1):
                    parameters.append(cal.get(data).get(i))
            return parameters
        else:
            return "Выходные"

if __name__ == '__main__':
    print(date_now().para_return())