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

    @bot.message_handler(commands=['reg'])
def start_reg(message):
    msg = bot.send_message(message.chat.id, "Как тебя зовут, герой?")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    name = message.text
    msg = bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! А какая у тебя суперсила?")
    bot.register_next_step_handler(msg, process_power_step)

def process_power_step(message):
    power = message.text
    bot.send_message(message.chat.id, f"Записал: {power}. Теперь я знаю о тебе всё!")@bot.message_handler(commands=['reg'])
def start_reg(message):
    msg = bot.send_message(message.chat.id, "Как тебя зовут, герой?")
    bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    name = message.text
    msg = bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! А какая у тебя суперсила?")
    bot.register_next_step_handler(msg, process_power_step)

def process_power_step(message):
    power = message.text
    bot.send_message(message.chat.id, f"Записал: {power}. Теперь я знаю о тебе всё!")


@bot.message_handler(commands=['clear'])
def delete_msg(message):
    # Удаляет сообщение пользователя, которое содержало команду
    bot.delete_message(message.chat.id, message.message_id)
    
    # Отправляет новое и удаляет его через 5 секунд
    tmp = bot.send_message(message.chat.id, "Это сообщение самоликвидируется...")
    import threading
    threading.Timer(5, lambda: bot.delete_message(message.chat.id, tmp.message_id)).start()

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Ого, классное фото! Сохраню себе в архив Лиги Справедливости.")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    bot.reply_to(message, "Я слышу твой голос, но пока не научился распознавать речь. Попробуй написать текстом!")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request) # Передаем запрос дальше
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Запрос обработан за: {process_time:.4f} сек")
    return response