from datetime import timedelta, datetime, timezone
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject
import asyncio
from data import data
from zoneinfo import ZoneInfo
db = data()
db.start()
idd = {
    1 : 1528266799,
    2 : 1522348807
}
API_TOKEN = '7652049176:AAEk6LMwxKSpzPFSa3fySdZ8PHzh69Wdhzg'
chat_id = '-1002228889442'
test_id = '-1002419689146'
bot = Bot(token = API_TOKEN)
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
    elif args[0].lower() == "all":
        await message.answer(f"{days[db.data_weekly() - 1]}\n1: {db.para(1)}\n2: {db.para(2)}\n3: {db.para(3)}\n4: {db.para(4)}")
    elif args[0].lower() == "next":
        await message.answer(f"{days[db.data_weekly()]}\n1: {db.para(1, 1)}\n2: {db.para(2, 1)}\n3: {db.para(3, 1)}\n4: {db.para(4, 1)}")

@dp.message(Command("papa"))
async def papa(message: Message):
    await message.answer("Нету у тебя папы.")

@dp.message(Command("mama"))
async def mama(message: Message):
    await message.answer("Нету у тебя мамы.")

@dp.message(Command("otmena"))
async def otmena_pari(message: Message):
    if message.from_user.id == idd.get(1) or idd.get(2):
        db.otmena()
        text = "Параметр: <b>Отмена Пары</b> успешно поставлен!"
        await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command("test"))
async def test(message : Message, command: CommandObject):
    pass

@dp.message(Command("whping"))
async def test(message : Message, command: CommandObject):
    args = command.args
    db.read_file()
    db.wh_arg = True
    asyncio.create_task(tuzyara2(message, args))
    await asyncio.sleep(5)
    db.wh_arg = False

async def tuzyara2(message : Message, args):
    while db.wh_arg:
        await message.answer(f"@{args} - пингатуло?")
        await asyncio.sleep(0.3)

@dp.message(Command("testping"))
async def testping(message : Message):
    db.read_file()
    text = "@" + db.username[0]
    if len(db.username) > 1:
        for i in range(1, len(db.username)):
            text = f"{text}, @{db.username[i]}"
    await message.reply(text)
    
@dp.message(Command("pingme"))
async def pingme(message : Message):
    db.ping(message)

@dp.message(Command("pingwho"))
async def pingwho(message : Message):
    db.read_file()
    if len(db.all) == 0:
        await message.answer("Нет кого пинговать.")
    else:
        text = "Вот всё кого будет пинговать: " + db.username[0]
        if len(db.username) > 1:
            for i in range(1, len(db.username)):
                text = f"{text}, {db.username[i]}"
        await message.reply(text)

@dp.message(Command("delete"))
async def delete(message : Message):
    if message.from_user.id == idd.get(1) or idd.get(2):
        with open("ping.txt", "w") as f:
            pass

@dp.message(Command("new"))
async def new(message : Message, command: CommandObject):
    args = command.args
    print(args)
    with open("ping.txt", "w") as file:
        file.write(str(args))

@dp.message(Command("last"))
async def last(message : Message):
    if message.from_user.id == idd.get(1) or idd.get(2):
        with open("ping.txt", "r") as file:
            await bot.send_message(chat_id=test_id, text=f"last\n{file.read()}")

async def send_message():
    try:
        db.read_file()
        username = db.username
        text = "@" + username[0]
        print(username, len(username))
        if len(username) > 1:
            for i in range(1, len(username)):
                text = f"{text} @{username[i]}"
        await bot.send_message(chat_id=chat_id, text=f"Пара некст - {db.para()}.\nСсылка - {(db.get_url()) if db.para() != "Пары нет" else None}.")
        await bot.send_message(chat_id=chat_id, text=f"Пинг: {text}")
        print(f"Сообщение отправлено в {datetime.now().strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

async def scheduler(target_times: list):
    utc_plus_2 = ZoneInfo("Europe/Kiev")
    while True:
        now = datetime.now(utc_plus_2)
        future_targets = []
        for time_str in target_times:
            target_hour, target_minute = map(int, time_str.split(":"))
            target = now.replace(
                hour=target_hour,
                minute=target_minute,
                second=0,
                microsecond=0
            )
            if now > target:
                target += timedelta(days=1)
            future_targets.append(target)
        next_target = min(future_targets)
        wait_seconds = (next_target - now).total_seconds()
        print(f"Ожидание до {next_target.strftime('%H:%M')} UTC+2 ({wait_seconds:.0f} секунд)")
        await asyncio.sleep(wait_seconds)
        await send_message()

async def on_startup():
    asyncio.create_task(scheduler(["08:28", "09:58", "11:58", "13:25"]))

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
