# Объяснение кода понятными словами.
____
Есть 3 файла `main.py`, `data.py`, `date_for_now.py`.

В `main.py` использует функции для вычесление какая сейчас пара из файла `data.py`.

А `data.py` просто обобщает, сам по себе он ничего не вычисляет, просто приводит в кучу все базовые и раздробленые функции из `date_for_now.py`.

И ещё в `data.py` хранится расписание пар, ссылки на эти пары, и ещё пару вещей для вычисление тип недели, оменили ли пару, и всё.

и самый последний файл это `date_for_now.py` в нём как раз и происходит вычисление вся нам нужная информация, это: какая сейчас пара по номеру

какая именно пара (название), тип недели, время по utc. И начнем разбор именно с этого файлика.:blush:

Мы возьмем все функции и каждую по отдельности разберём.

![фотка на функции](https://i.imgur.com/gI3G4cB.png)

____

Первая `date_return` (я ещё в каждую фунцию коменнтарии добавил).

```python
def date_return(self):
    res = datetime.datetime.now()
    return int(res.isoweekday())
```

Функция возвращает сегоднешний день недели:

| День недели | Вывод |
|------------|-------|
| Понедельник | 1     |
| Вторник    | 2     |
| Среда      | 3     |
| Четверг    | 4     |
| Пятница    | 5     |

Реализовано очень просто получаем сегодняшний день, и через функцию `isoweekday` получаем день недели, если убрать в начале `is`,

то получим функцию `weekday()` и она будет возвращать всё тоже самое только результат будет на **1** меньше. 

____

Следующая функция это `full_date_return`.

```python
def full_date_return(self, _now = 0, day = 10, mounth = 2):
    cogda_mounth, cogda_day = mounth, day
    mounth = int(datetime.datetime.now().strftime("%m"))
    day = int(datetime.datetime.now().strftime("%d"))
    year = int(datetime.datetime.now().strftime("20%y"))
    now = int(1) if _now == 0 else int(0)
    for i in range(mounth - cogda_mounth + 1):
        for j in range(1, calendar.monthrange(year, i + cogda_mounth)[1] + 1):
            if i == 0 and j <= cogda_day - 1:
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
```

Для неё импортируется библеотека `calendar` по позже объясню зачем.

Начнем с начало, это функция возвращает какой сейчас тип недели (численный, знаменатель).

в начале мы получаем 3 параметра:

| Ввод ||