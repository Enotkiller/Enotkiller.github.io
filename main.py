#файл пидора
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
import logging
import asyncio
from data import data
db = data()
db.start()
idd = {
    1 : 1528266799,
    2 : 1522348807
}
url = {
    "Биология" : "https://meet.google.com/eed-rtog-srd?authuser=4&hs=179",
    "Химия" : "https://meet.google.com/cut-rvao-zbt?authuser=4&hs=179",
    "Оборона Украины" : "https://meet.google.com/uqv-omtr-bwx?authuser=4&hs=179",
    "Физра" : "https://meet.google.com/mxt-wvmr-gny?authuser=4&hs=179",
    "Английский" : "1 Группа: https://meet.google.com/svs-snwo-tfm?authuser=4&hs=179\n2 Группа: ",
    "Математика" : "https://us02web.zoom.us/j/84351065107?pwd=WOrdR7On7gbcrPynf178H0A9FW3M3k.1",
    "Зарубежная литература" : "https://meet.google.com/mnx-uxwk-wgo?authuser=4&hs=179",
    "История Украины" : "https://meet.google.com/zww-totu-kva?authuser=4&hs=179",
    "География" : "https://meet.google.com/gyc-nwne-nvi?authuser=4&hs=179",
    "Физика" : "https://meet.google.com/znu-moir-atb?authuser=4&hs=179",
    "Информатика" : "https://meet.google.com/kwt-xdbj-kdq?authuser=4&hs=179",
    "Украинский язык" : "https://meet.google.com/jkz-wqku-xyh?authuser=4&hs=179",
    "Украинская литература" : "https://meet.google.com/nem-mhnk-ghe?authuser=4&hs=179",
    "Всемирная история" : "https://meet.google.com/qay-vxca-jfw?authuser=4&hs=179"
}
bot = Bot(token = '7080600577:AAHIKU7SrX8XmQrcnZlb5fLtVjOtAdHt-NU')
dp = Dispatcher()
datenow = db.data_weekly()
days = ["Понедельник", "Вторник", "Среда", "Четвегр", "Пятница"]
@dp.message(Command("para"))
async def cmd_start(message: Message):
    if datenow <= 5 and db.time_float() <= 14.50:
        await message.answer(f"{days[datenow - 1]}\nТекущее время: {db.time()}\n{"Текущая" if not db.peremena() else "Будет"} пара: {db.para()}\nСтатус: {("Отпустили" if db.otmena_now() == 1 else "Перемена" if db.peremena() else "Идёт") if db.para() != "Пары нет" else "Ничего нет"}\nСсылка: {url.get(db.para())}")
    else:
        await message.answer("Какие уроки челл.")
@dp.message(Command("otmena"))
async def otmena_pari(message: Message):
    if message.from_user.id == idd.get(1) or idd.get(2):
        db.otmena()
        text = "Параметр: <b>Отмена Пары</b> успешно поставлен!"
        await message.answer(text, parse_mode=ParseMode.HTML)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
