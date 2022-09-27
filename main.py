import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def stop(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Stop")


if __name__ == '__main__':
    application = ApplicationBuilder().token('5318589168:AAHji914LUBoYbIrwnfv3RFsL-me7KJcOFU').build()

    start_handler = CommandHandler('start', start)
    stop_handler = CommandHandler('stop_the_bot', stop)
    application.add_handler(start_handler)
    application.add_handler(stop_handler)

    application.run_polling(stop_signals=None)