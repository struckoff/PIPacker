import logging
import telegram.ext as t
import packager

GRANT_ACCESS = ('SoHuman',)


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
    )

updater = t.Updater(token='608719426:AAGlxr8ooxbwmuCsFZLVZjXNVdLwB9YdVPQ')
dispatcher = updater.dispatcher

def access_wrapper(func):
    def wrapper(bot, update):
        if update.effective_user in GRANT_ACCESS:
            return func(bot, update)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='I don`t know you')
    return wrapper


@access_wrapper
def start(bot, update):
    print(update.effective_user)
    bot.send_message(chat_id=update.message.chat_id, text='Sup, wanna some packages ?')



start_handler = t.CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()