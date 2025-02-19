import datetime
import calendar

class date_now:
    def date_return(self):
        res = datetime.datetime.now()
        return int(res.isoweekday())
    def full_date_return(self, _now = 1, day = 10, mounth = 2):
        cogda_mounth, cogda_day = mounth, day
        mounth = int(datetime.datetime.now().strftime("%m"))
        day = int(datetime.datetime.now().strftime("%d"))
        year = int(datetime.datetime.now().strftime("20%y"))
        now = _now
        for i in range(mounth - cogda_mounth + 1):
            for j in range(1, calendar.monthrange(year, i + cogda_mounth)[1] + 1):
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
        year = int(datetime.datetime.now().strftime("20%y"))
        date = datetime.date(year, mounth, day)
        return date.isoweekday()
    def time_return(self, x = 2):

        time = datetime.datetime.now().strftime("%H:%M")
        time = str(f"{int(time.split(":")[0]) + x}:{time.split(":")[1]}")
        return time
    def quest_return(self, _time):
        data = _time.split(":")
        time = float(f"{data[0]}.{data[1]}")
        if time >= 8.0 and time <= 9.49:
            if time >= 8.0 and time <= 8.30:
                return -1
            else:
                return 1
        elif time >= 9.50 and time <= 11.20:
            if time >= 9.50 and time <= 9.59:
                return -2
            else:
                return 2
        elif time >= 11.20 and time <= 13.20:
            if time >= 11.20 and time <= 11.59:
                return -3
            else:
                return 3
        elif time >= 13.20 and time <= 14.50:
            if time >= 13.20 and time <= 13.29:
                return -4
            else:
                return 4
    def perema_now_retuen(self, quest):
        if quest < 0:
            return True
        else:
            return False
    def para_return(self, data, quest, cal, full_date):

        parameters = None
        if data <= 5:
            for i in range(1, 4 + 1):
                if quest == i or quest == i * -1:
                    if full_date == 1:
                        parameters = cal.get(data).get(i)
                    else:
                        if cal.get(data).get(float(f"{i}.5")) is None:
                            parameters = cal.get(data).get(i)
                        else:
                            parameters = cal.get(data).get(float(f"{i}.5"))

            if parameters != None:
                return parameters
            else:
                return "Пары нет"
        else:
            return "Выходные"

if __name__ == '__main__':
    print(date_now().full_date_return())
