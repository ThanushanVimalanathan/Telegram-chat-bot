import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


#my bot name is my2000bot_bot.
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


#Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message:types.Message):
    #this handler recive message with /start or /help command
    
    await message.reply("Hi\n I am Echo Bot!\n Enna venum Unakku ?.")
    

@dp.message_handler()
async def echo(message:types.Message):
    #This will return echo
    
    await message.answer(message.text)




    
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)