from os import getenv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
  start_buttons = ['Moscow', 'Orenburg']
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  keyboard.add(*start_buttons)

  await message.answer('Select a city', reply_markup=keyboard)


if __name__ == '__main__':
  executor.start_polling(dp)
