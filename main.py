from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# .env ফাইল থেকে টোকেন লোড করা
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Start কমান্ডের জন্য ফাংশন
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(text="🌐 Open App", web_app=WebAppInfo(url="https://qerion-miner.onrender.com"))],
        [InlineKeyboardButton(text="👥 Join Community", url="https://t.me/airdrop9810")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 Welcome to Qerion Miner!", reply_markup=markup)

# বট চালানোর জন্য মূল ফাংশন
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

# প্রোগ্রাম চালানোর জন্য
if __name__ == "__main__":
    main()
