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
bot = Bot(token = '7080600577:AAHIKU7SrX8XmQrcnZlb5fLtVjOtAdHt-NU')
dp = Dispatcher()
datenow = db.data_weekly()
days = ["Понедельник", "Вторник", "Среда", "Четвегр", "Пятница"]
@dp.message(Command("para"))
async def cmd_start(message: Message):
    if datenow <= 5 and db.time_float() <= 14.50:
        await message.answer(f"{days[datenow - 1]}\nТекущее время: {db.time()}\n{"Текущая" if not db.peremena() else "Будет"} пара: {db.para()}\nСтатус: {("Отпустили" if db.otmena_now() == 1 else "Перемена" if db.peremena() else "Идёт") if db.para() != "Пары нет" else "Ничего нет"}")
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
