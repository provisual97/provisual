from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from datetime import datetime
updater = Updater(token='325809142:AAEwXMx6vA6YiVzLSyFlZ1ON8Jy9j1yqfRs')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello")
 
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
updater.stop()
