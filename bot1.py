import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

bot = Bot(token="8665498939:AAFH3rf6JaoxFVvMvdNlIOk0HJLAoiNkX0U")
dp = Dispatcher()

@dp.message(Command("start", "help"))
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я работаю на aiogram 3.x")

@dp.message(Command("command"))
async def process_custom_command(message: types.Message):
    await message.reply("Вы вызвали команду /command")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")