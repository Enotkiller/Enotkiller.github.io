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
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
@dp.message(Command("para"))
async def cmd_start(message: Message):
    print(message.from_user.username, message.from_user.id)
    if db.data_weekly() <= 5 and db.time_float() <= 14.50 and message.from_user.id != 5376094724:
        await message.answer(f"{days[db.data_weekly() - 1]}\nТекущее время: {db.time()}\n{"Текущая" if not db.peremena() else "Будет"} пара: {db.para()}\nСтатус: {(("Отпустили" if db.otmena_now() == 1 else "Перемена" if db.peremena() else ("Идёт") if message.from_user.id != 7250542929 else "Не идёт, а летит") if db.para() != "Пары нет" else "Ничего нет")}\nСсылка: {db.get_url()}")
    elif message.from_user.id == 5376094724:
        await message.answer(f"Картель вызван...\nВремя: {db.time()}\nОписание к заказу: лиж бы все, но не {db.para()}")
    else:
        await message.answer("Какие уроки челл.")
@db.message(Command("papa"))
async def papa(message: Message):
    await message.answer("Нету у тебя папы.")
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
