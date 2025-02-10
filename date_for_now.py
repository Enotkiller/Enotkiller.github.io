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
            return 1
        elif time >= 9.5 and time <= 11.20:
            return 2
        elif time >= 11.20 and time <= 13.20:
            return 3
        elif time >= 13.20 and time <= 14.50:
            return 3

if __name__ == '__main__':
    pass