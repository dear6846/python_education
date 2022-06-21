
import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfod_lugati import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '5415240053:AAFbLe9HTSYlLS4YpwYKSalPEIc1PY18vxM'

    # Configure logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        """
         This handler will be called when user sends `/start`  command
        """
        await message.reply("Hello!\n welcome to translator")


@dp.message_handler()
async def tarjimon(message: types.Message):
          lang = translator.detect(message.text).lang
          if len(message.text.split()) > 2:
             dest = 'ru' if lang == 'en' else 'en'
             await message.reply(translator.translate(message.text, dest).text)

          else:
                 if  lang=='en':
                  word_id = message.text
                 else:
                  word_id = translator.translate(message.text, dest='en').text
                 lookup = getDefinitions(word_id)
                 if lookup:
                  await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
                 if lookup.get('audio'):
                   await message.reply_voice(lookup['audio'])
                 else:
                  await message.reply("Bunday so'z topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)