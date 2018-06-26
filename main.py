import logging
import telegram.ext as t


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
    )

updater = t.Updater(token='608719426:AAGlxr8ooxbwmuCsFZLVZjXNVdLwB9YdVPQ')
dispatcher = updater.dispatcher

def start(bot, update):
    print(update.effective_user)
    bot.send_message(chat_id=update.message.chat_id, text='Sup, wanna some packages ?')



start_handler = t.CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()