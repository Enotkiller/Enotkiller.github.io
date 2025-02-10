#файл пидора
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import logging
import asyncio
bot = Bot(token = '7080600577:AAHIKU7SrX8XmQrcnZlb5fLtVjOtAdHt-NU')
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer('qq')
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())