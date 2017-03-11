from telegram.ext import Updater , CommandHandler, MessageHandler, Filters
def greet_user(bot, update):
	print('Loaded /start')
	#print(update)
	bot.sendMessage(update.message.chat_id, text = 'Lets talk')
def show_error(bot, update, error):
	print(error)
def talk_to_me(bot, update):
	print(update.message.text)
	bot.sendMessage(update.message.chat_id, update.message.text)

def main():
	updater = Updater("358140435:AAFfh9v3EzZoMEyjI6bAbncZ78Qmq80HUnY")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start",greet_user))
	dp.add_error_handler(show_error)
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()
main()
