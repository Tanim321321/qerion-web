
import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os 

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_keyboard = [
        [
            InlineKeyboardButton("🌐 Open App",web_app=WebAppInfo(url="https://qerion-miner.onrender.com"))
        ]
    ]
    inline_keyboard = [
        [
            InlineKeyboardButton("👥 Join Community", url="https://t.me/airdrop9810")
        ]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)
await update.message.reply_text("Welcome to Qerion Miner!",reply_markup=inline_markup)
   

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
