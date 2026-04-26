from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8379855214:AAH3BZqlKW8d6-qS8cSujr-IEX3PnBiyGoA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp)