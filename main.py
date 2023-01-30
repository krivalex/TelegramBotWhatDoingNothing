import telebot

bot = telebot.TeleBot('5958468688:AAGyrVQpELj4cwbir9k-FRtJAPGuQP-7QBk')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['crash'])
def crash(message):
    crash_value = 10 / 0

  
bot.infinity_polling()
