from telegram.ext import Updater


def main():
    mybot = Updater("879930187:AAHumZT82IE7bJAFIUtkbAfczgSnhgdyB6Q")
    mybot.start_polling()
    mybot.idle()

   
main()
