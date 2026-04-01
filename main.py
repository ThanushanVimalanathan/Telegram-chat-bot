
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import openai
import os
import sys

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")



class Reference:
    
    def __init__(self) -> None:
        self.response = ""


reference = Reference()
model_name = "gpt-3.5-turbo"

#Initialize telegram bot
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message:types.Message):
    #this handler recive message with /star command
    
    await message.reply("Hi\n I am Echo Bot!\n Enna venum Unakku ?.")
    
    
    
def clear_past():
    reference.response = ""
    
    
@dispatcher.message_handler(commands=['clear'])
async def clear(message:types.Message):
    # help menu handler
    
    clear_past()
    await message.reply("I've cleared the past conversation and context.")  


@dispatcher.message_handler(commands=['help'])
async def command_start_handler(message:types.Message):
    # help menu handler
    
    help_command = """
    
    HI There, I'm chtGPT Telegram Bot created by Shaan! so plese follow these commands - 
    /start - to start conversation
    /clear - to clear the past chat
    /help  - to get this help menu.
    I hope this helps. :)
    
    """
    await message.reply(help_command)    
    
    
    
@dispatcher.message_handler()
async def chatgpt(message:types.Message):
    #generate response from user input
    
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = model_name,
        messages = [
            {"role":"assistant","content":reference.response},
            {"role":"user","content":message.text}
        ]
    )
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)    
    
    
if __name__ == "__main__":
    executor.start_polling(dispatcher,skip_updates=True)
