from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7968961400:AAEVDteHzEk0hlTGwNr4H6okb1xc3B_CkME"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="🌐 Open App",
                web_app=WebAppInfo(url="https://qerion-miner.onrender.com")
            )
        ],
        [
            InlineKeyboardButton(
                text="👥 Join Community",
                url="https://t.me/airdrop9810"
            )
        ]
    ])
    await update.message.reply_text("👋 Welcome to Qerion Miner!", reply_markup=keyboard)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
