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

if __name__ == '__main__':
    pass