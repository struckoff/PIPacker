import logging
import telegram.ext as t
import packager
import os
import packager


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
def start_handler(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Sup, wanna some packages ?')

def prepare_package(package_name):
    package_source = packager.download_package(package_name, 'packages')
    zip_path = packager.pack(package_name, package_source)
    return zip_path

@access_wrapper
def prepare_package_handler(bot, update):
    package_name = update.message.text
    logging.info(package_name)
    if package_name is not None and len(package_name) > 0:
        zip_path = prepare_package(package_name)
        bot.send_document(chat_id=update.message.chat_id, document=open(zip_path, 'rb'))
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Something wrong')


updater.dispatcher.add_handler(t.CommandHandler('start', start_handler))
updater.dispatcher.add_handler(t.MessageHandler(t.Filters.text, callback=prepare_package_handler))

if __name__ == '__main__':
    updater.start_polling()
    if not updater.running:
        exit(1)