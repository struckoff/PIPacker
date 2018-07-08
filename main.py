import logging
import telegram.ext as t
import packager
import os


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
    )

GRANT_ACCESS = (os.getenv('TELEGRAM_USERNAME'),)
TOKEN = os.getenv('TELEGRAM_BOT_API')

def make_updater():
    return t.Updater(token=TOKEN)

updater = make_updater()

def access_wrapper(func):
    def wrapper(bot, update):
        if update.effective_user['username'] in GRANT_ACCESS:
            return func(bot, update)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='I don`t know you')
    return wrapper


@access_wrapper
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Sup, wanna some packages ?')


start_handler = t.CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

if __name__ == '__main__':
    updater.start_polling()
    if not updater.running:
        updater.stop()
        exit(1)