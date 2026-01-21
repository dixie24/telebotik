import telebot
from telebot import types 


import telebot
from telebot import types

# Замени 'ТВОЙ_ТОКЕН' на токен от @BotFather
bot = telebot.TeleBot('ТВОЙ_ТОКЕН')

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, Супермен! Я готов к работе.")

# Пример обработки любого текста
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Ты написал: " + message.text)

# Запуск бота (будет работать, пока не выключишь программу)
bot.infinity_polling()