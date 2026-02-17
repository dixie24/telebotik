import telebot 


TOKEN = "8551310109:AAE9wuLxosdtCE9SI9PYzin5n_SfE2O-ER0"

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


@bot.message_handler(content_types=['text', 'photo', 'document'])
def handle_content_types(message):
    bot.reply_to(message, f"Received a message of type: {message.content_type}")


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    bot.reply_to(message, "Bot is stopping...")
    bot.stop_polling()

@bot.message_handler(commands=['restart'])
def restart_bot(message):
    bot.reply_to(message, "Bot is restarting...")
    bot.stop_polling()
    bot.infinity_polling()


@bot.message_reaction_count_handler(func=lambda message: message.reactions and len(message.reactions) > 0)
def handle_reactions(message):
    bot.reply_to(message, f"Received {len(message.reactions)} reactions!")


@bot.add_business_connection_handler(commands=['business'])
def handle_business_connection(message):
    bot.reply_to(message, "Business connection handler triggered!")

@bot.message_handler(content_types=['text', 'photo', 'document'])
def handle_content_types(message):
    bot.reply_to(message, f"Received a message of type: {message.content_type}")

print("Bot is running...")
bot.infinity_polling()