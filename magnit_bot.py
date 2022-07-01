from os import getenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
  await message.answer('Privet!')


if __name__ == '__main__':
  executor.start_polling(dp)
