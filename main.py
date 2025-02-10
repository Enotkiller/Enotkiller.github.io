#файл пидора
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import logging
import asyncio
from data import data
db = data()
db.start()
bot = Bot(token = '7080600577:AAHIKU7SrX8XmQrcnZlb5fLtVjOtAdHt-NU')
dp = Dispatcher()
datenow = db.data
days = ["Понедельник", "Вторник", "Среда", "Четвегр", "Пятница"]
@dp.message(Command("para"))
async def cmd_start(message: Message):
    if datenow <= 5 and db.time_float() <= 14.50:
        await message.answer(f"{days[datenow]}\nТекущее время: {db.time()}\nТекущая пара: {db.para()}\nСтатус: {db.peremena()}")
    else:
        await message.answer("Какие уроки челл.")

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
