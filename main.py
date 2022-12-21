from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5650424674:AAGPs-FVez4B4ehEBoespe2-AzJEQ-CQndY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ бот DZ!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.")
async def echo(message: types.Message):
   await message.answer(message.text)

   if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
