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



@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🚀 Мой профиль")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выбери пункт меню:", reply_markup=markup)