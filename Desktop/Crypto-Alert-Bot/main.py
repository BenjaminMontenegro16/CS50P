from dotenv import load_dotenv
import os
from telegram.ext import CommandHandler, Application, ContextTypes
import asyncio
import requests

async def post_init(app):
    asyncio.create_task(loop(app))

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")
app = Application.builder().token(token).post_init(post_init).build()

COINS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "BNB": "binance-coin",
    "XRP": "xrp",
    "ADA": "cardano",
    "DOGE": "dogecoin",
    "DOT": "polkadot",
    "MATIC": "matic-network",
    "LTC": "litecoin",
    "AVAX": "avalanche",
    "LINK": "chainlink",
    "UNI": "uniswap",
    "ATOM": "cosmos",
    "XLM": "stellar",
    "ALGO": "algorand",
    "VET": "vechain",
    "FIL": "filecoin",
    "TRX": "tron",
    "ETC": "ethereum-classic",
    "HBAR": "hedera-hashgraph",
    "SAND": "the-sandbox",
    "MANA": "decentraland",
    "AAVE": "aave",
    "GRT": "the-graph",
    "EOS": "eos",
    "THETA": "theta-token",
    "NEO": "neo",
    "EGLD": "elrond-erd-2",
    "FTM": "fantom"
}

async def start(update, context):
    await update.message.reply_text("Hi, im the Crypto Alert Bot, if you don't know how to use me type /info.")

app.add_handler(CommandHandler("start", start))

async def info(update, context):
    
    text_info = (
    "📊 *CryptoAlertBot* — Price Alerts\n\n"
    "*Available commands:*\n"
    "/alert BTC 80000 — Set an alert for when BTC reaches $80,000\n"
    "/my_alerts — View your active alerts\n"
    "/delete_alerts — Delete all your alerts\n\n"
    "*Supported coins:* BTC, ETH, SOL\n\n"
    "💡 You'll get notified the moment your target price is hit!"
)
    await update.message.reply_text(text_info, parse_mode="Markdown") 


app.add_handler(CommandHandler("info", info))


def get_price(coin):
    api_key = os.getenv("API-KEY")

    
    answer = requests.get(f"https://rest.coincap.io/v3/assets/{COINS[coin]}?apiKey={api_key}")
    price = float(answer.json()["data"]["priceUsd"])
    return price



alerts = []

async def alert(update, context):
    try:
        coin = context.args[0]
        target = float(context.args[1])

        
        alerts.append({
        "user_id": update.effective_user.id,
        "coin": coin,
        "target": float(target),
        })

        await update.message.reply_text(f"I've set a notification for when {coin} gets to {target} ")

    except (ValueError, KeyError):
        await update.message.reply_text(f"Maybe you forgou the Coin or the amount?")

    except requests.RequestException:
        await update.message.reply_text(f"Network Problem")

app.add_handler(CommandHandler("alert", alert))


async def loop(app): 
    while True:
        for alerta in alerts:
            current_price = get_price(alerta["coin"])
            if current_price >= alerta["target"]:
                await app.bot.send_message(chat_id=alerta["user_id"], text=f"{alerta['coin']} It's currently on {alerta['target']}, time to buy!")
            
        await asyncio.sleep(60)


async def deletealerts(update, context):
    user_id = update.effective_user.id
    alerts[:] = [a for a in alerts if a["user_id"] != user_id]
    await update.message.reply_text("All your alerts has been deleted")
    alerts.remove(alerts)

app.add_handler(CommandHandler("deletealerts", deletealerts))


async def myalerts(update, context):
    user_id = update.effective_user.id
    show = [a for a in alerts if a["user_id"] == user_id]
    if not show:
        await update.message.reply_text("You have no active alerts.")
        return

    text = "📋 *Your active alerts:*\n"
    for a in show:
        text += f"• {a['coin']} → ${a['target']:,.0f}\n"

    await update.message.reply_text(text, parse_mode="Markdown")


app.add_handler(CommandHandler("myalerts", myalerts))



app.run_polling()