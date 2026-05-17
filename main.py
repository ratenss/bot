import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openpyxl import Workbook

# 1. ТВОЙ ТОКЕН ОТ @BotFather (никогда не выкладывай его в интернет!)
API_TOKEN = ''

# 2. Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

name = ''

sprint = 'Спринт'
sred = 'Средние дистанции'
dlin = 'Длинные дистанции'
est = 'Эстафета'

# 3. Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я запишу тебя на марафон!")

# 4. Обработчик для любого текстового сообщения (эхо)
@dp.message()
async def echo(message: types.Message):
    # Отправляем обратно тот же текст
    await message.answer(message.text)

@dp.message(Command("add"))
async def add(message: types.Message):
    name = input("Введи своё ФИО: \n")
    type = input("Введи тип марафона: \nДоступный выбор: {sprint}, {sred}, {dlin}, {est}\n")
    if type == "":
        sprint = 'Спринт'
    elif type == "":
        sred = 'Средние дистанции'
    elif type == "":
        dlin = 'Длинные дистанции'
    elif type == "":
        est = 'Эстафета'
    else: print("Введён неверный тип марафона!")
    await message.answer("Введённые данные:\nФИО: {name}\nТип забега: {type}")

# 5. Запуск бота
async def main():
    print("Бот запущен...")
    # Запускаем long polling
    await dp.start_polling(bot)

    """# сохранение результатов в .xlsx
    if all_products:
        # создание новой Excel-книги
        wb = Workbook()
        ws = wb.active
        ws.title = "Оперативная память"

        # добавление заголовки столбцов
        ws.append(['Название', 'Цена', 'Ссылка'])

        # добавление данных о каждом товаре
        for product in all_products:
            ws.append([product['title'], product['price'], product['link']])

        # сохранение файла
        filename = 'operativnaya_pamyat.xlsx'
        wb.save(filename)"""

if __name__ == "__main__":
    asyncio.run(main())
