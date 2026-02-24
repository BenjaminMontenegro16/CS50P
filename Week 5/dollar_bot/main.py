from dotenv import load_dotenv
import os
from telegram.ext import CommandHandler, Application
import requests

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")
app = Application.builder().token(token).build()

async def dollar(update, context):
    try:
    
        currency = context.args[1]
        value = float(context.args[0])
        answer = get_currencies(value)
        rates = answer["rates"]
        result = rates[currency.upper()]
        await update.message.reply_text(f"{value} USD = {result} {currency.upper()}")

    except IndexError:
        await update.message.reply_text("Maybe you forgot the currency or the amount.?")
    except (KeyError, ValueError):
        await update.message.reply_text(f"Writte a real number, please.")
def get_currencies(value):
    response = requests.get(f"https://api.frankfurter.app/latest?amount={value}&from=USD")
    return response.json()


app.add_handler(CommandHandler("dollar", dollar))


async def start(update, context):
    await update.message.reply_text("Hi ! Wellcome to the dollar to currencies bot, if you don't know how to use me type /info.")
    
app.add_handler(CommandHandler("start", start))


def get_name_currencies():
    names = requests.get("https://api.frankfurter.app/currencies")
    return names.json()


async def info(update, context):
    names_dict = get_name_currencies()
    
    message = "<b>Available Currencies:</b>\n\n"
    
    for code, name in names_dict.items():
        message += f"• <code>{code}</code>: {name}\n"
    

    await update.message.reply_html(message)


app.add_handler(CommandHandler("info", info))



app.run_polling()

#I finally made my first Telegram Bot, I hope i can sell these bots, not this one, this is just a demo of all the projects 
#i want to make, but anyways, i don't know who would want to buy this bot but if you want it just text me at my X: @BenjaMon_Dev. 

#PD: The bot will be runnig untill i just end it, so if it doesnt work its because its outdated :)

