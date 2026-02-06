import telebot 


TOKEN = "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Hello my friend {message.from_user.first_name}!")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This is a help message!")

@bot.message_handler(commands=['fuck u hoe'])
def send_insult(message):
    bot.reply_to(message, "I'm sorry, but U stupid ass bitch!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.infinity_polling()