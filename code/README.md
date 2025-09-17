# Здесь весь код бота.

____ 

В [`Bot.py`](/code/Bot.py) - как неожидано там лежит телеграм бот.
В [`DataBase.py`](/code/DataBase.py) - загружает все конфики, а после загружает в redis.
В [`System.py`](/code/System.py) - работа с `DataBase.py`, делает разчеты.
В [`Debug.py`](/code/Debug.py) - лежит функция `print_debug`, её вызывают все функции для вывода `debug` сообщений.