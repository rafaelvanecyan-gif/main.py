import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 7747583993:AAEr1--0D3VJpy4xZI-OZy8dxQeHLia7KgM

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твоя виртуальная половинка ❤️")

# Ответ на обычные сообщения
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    reply = f"Ты написал: {text}\nА я отвечу так: я рядом 💕"
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    app.run_polling()

if __name__ == "__main__":
    main()
