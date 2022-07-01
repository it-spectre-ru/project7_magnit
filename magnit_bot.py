from os import getenv
from main_async import collect_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiofiles import os

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
  start_buttons = ['Moscow', 'Orenburg']
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  keyboard.add(*start_buttons)

  await message.answer('Select a city', reply_markup=keyboard)

@dp.message_handler(Text(equals='Moscow'))
async def moscow_city(message: types.Message):
  await message.answer('Waiting...')
  chat_id = message.chat.id
  await send_data(city_code='2398', chat_id=chat_id)


@dp.message_handler(Text(equals='Orenburg'))
async def orb_city(message: types.Message):
  await message.answer('Waiting...')
  chat_id = message.chat.id
  await send_data(city_code='2403', chat_id=chat_id)


async def send_data(city_code='2398', chat_id=''):
  file = await collect_data(city_code=city_code)
  await bot.send_document(chat_id=chat_id, document=open(file, 'rb'))
  await os.remove(file)


if __name__ == '__main__':
  executor.start_polling(dp)
