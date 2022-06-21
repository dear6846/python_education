import logging
import wikipedia


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5421661949:AAGhkLccH3gAGUhhlZ582vuDjonfP_nFb74'
wikipedia.set_lang('ru')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Добрый день!\nкакую информацию вы ищете.")



@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
           await message.answer('Мы не нашли информацию')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)