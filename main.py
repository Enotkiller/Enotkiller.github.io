#файл пидора
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
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
async def cmd_start(message: Message, command: CommandObject):
    args = (command.args.split()) if command.args != None else (command.args)
    if args == None:
        print(message.from_user.username, message.from_user.id)
        if db.data_weekly() <= 5 and db.time_float() <= 14.50 and message.from_user.id != 5376094724:
            await message.answer(f"{days[db.data_weekly() - 1]}\nТекущее время: {db.time()}\n{"Текущая" if not db.peremena() else "Будет"} пара: {db.para()}\nСтатус: {(("Отпустили" if db.otmena_now() == 1 else "Перемена" if db.peremena() else ("Идёт") if message.from_user.id != 7250542929 else "Не идёт, а летит") if db.para() != "Пары нет" else "Ничего нет")}\nСсылка: {db.get_url()}")
        elif message.from_user.id == 5376094724:
            await message.answer(f"Картель вызван...\nВремя: {db.time()}\nОписание к заказу: лиж бы все, но не {db.para()}")
        else:
            await message.answer("Какие уроки челл.")
    elif args[0].lower() != "all":
        await message.answer(f"{args[0]} Парой будет {db.para(now_p=int(args[0]))}.")
    elif args[0].lower() == "all":
        await message.answer(f"{days[db.data_weekly() - 1]}\n1: {db.para(1)}\n2: {db.para(2)}\n3: {db.para(3)}\n4: {db.para(4)}")
@dp.message(Command("test"))
async def test(message: Message, command: CommandObject):
    pass
@dp.message(Command("papa"))
async def papa(message: Message):
    await message.answer("Нету у тебя папы.")
# Обработчик команды /tagall
@dp.message(Command("tag"))
async def tag_all_members(message: Message):
    # Проверяем, что команда отправлена в группе или супергруппе
    if message.chat.type not in ["group", "supergroup"]:
        await message.reply("Эта команда работает только в группах!")
        return

    # Получаем ID чата
    chat_id = message.chat.id

    try:
        # Получаем список участников (до 200 за раз, можно увеличить с offset)
        members = []
        async for member in bot.get_chat_members(chat_id):
            # Пропускаем ботов и удалённые аккаунты
            if not member.user.is_bot and not member.user.is_deleted:
                members.append(member.user)

        if not members:
            await message.reply("В группе нет участников или у меня нет прав!")
            return

        # Формируем сообщение с упоминаниями
        mentions = []
        for user in members:
            if user.username:
                # Если есть username, используем его
                mentions.append(f"@{user.username}")
            else:
                # Если нет username, используем имя и ссылку по ID
                mentions.append(f"[{user.first_name}](tg://user?id={user.id})")

        # Разбиваем на части, если слишком много участников
        chunk_size = 50  # Количество упоминаний за раз (регулируй по длине сообщения)
        for i in range(0, len(mentions), chunk_size):
            chunk = " ".join(mentions[i:i + chunk_size])
            await bot.send_message(chat_id, f"Вызываю всех:\n{chunk}", parse_mode="Markdown")
            await asyncio.sleep(1)  # Задержка, чтобы не превысить лимиты Telegram

        await message.reply("Все участники упомянуты!")

    except Exception as e:
        await message.reply(f"Ошибка: {str(e)}")
@dp.message(Command("mama"))
async def papa(message: Message):
    await message.answer("Нету у тебя мамы.")
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
