#файл пидора
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import logging
import asyncio
from date_for_now import*
#fdsasa
bot = Bot(token = '7080600577:AAHIKU7SrX8XmQrcnZlb5fLtVjOtAdHt-NU')
dp = Dispatcher()
datenow = date_now().date_return()
timenow = date_now().time_return()
para = date_now().para_return()
@dp.message(Command("para"))
async def cmd_start(message: Message):
    if datenow == 1:
        await message.answer(f"Понедельник\nТекущее время: {timenow}\nТекущая пара: {para}")
    if datenow == 2:
        await message.answer(f"Вторник\nТекущее время: {timenow}\nТекущая пара: {para} ")
    if datenow == 3:
        await message.answer(f"Среда\nТекущее время: {timenow}\nТекущая пара: {para}")
    if datenow == 4:
        await message.answer(f"Четвегр\nТекущее время: {timenow}\nТекущая пара: {para}")
    if datenow == 5:
        await message.answer(f"Пятница\nТекущее время: {timenow}\nТекущая пара: {para}")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
