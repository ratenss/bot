import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

bot = Bot(token="8665498939:AAFH3rf6JaoxFVvMvdNlIOk0HJLAoiNkX0U")
dp = Dispatcher()

@dp.message(Command("start", "help"))
async def process_start_command(message: types.Message):
    await message.reply("Привет!\n\nЯ - Чат-бот записи на марафон.\n\nЕсли ты хочешь записаться на марафон жми /go")

@dp.message(Command("go"))
async def process_custom_command(message: types.Message):
    await message.reply("Отлично!\n\nДля записи на марафон требуется лишь твоё ФИО и тип забега.\n\n")

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