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


@app.post("/upload-map/")
async def upload_secret_map(file: UploadFile = File(...)):
    # file.filename - имя файла
    # file.file - сам объект файла для чтения
    contents = await file.read() 
    return {
        "filename": file.filename, 
        "size": len(contents),
        "content_type": file.content_type
    }

@bot.message_handler(func=lambda message: message.entities is not None)
def handle_links(message):
    for entity in message.entities:
        if entity.type == 'url':
            bot.reply_to(message, "Вижу ссылку! Главное, чтобы там не было ловушки с криптонитом. 🦸‍♂️")

            @bot.message_handler(commands=['share'])
def share_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # Кнопки запроса данных
    btn_phone = types.KeyboardButton("📱 Отправить номер", request_contact=True)
    btn_geo = types.KeyboardButton("📍 Отправить локацию", request_location=True)
    markup.add(btn_phone, btn_geo)
    bot.send_message(message.chat.id, "Супермен, подтверди свои координаты:", reply_markup=markup)

# Обработка полученной локации
@bot.message_handler(content_types=['location'])
def handle_location(message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.send_message(message.chat.id, f"Координаты получены: {lat}, {lon}. Вылетаю!")


@bot.message_handler(commands=['secret'])
def send_secret(message):
    text = (
        "*Важное сообщение:*\n"
        "||Тут секретный код от базы|| \n"
        "Поторопись, Супермен\!"
    )
    bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')

@bot.message_handler(commands=['album'])
def send_album(message):
    photo1 = 'https://example.com/photo1.jpg'
    photo2 = 'https://example.com/photo2.jpg'
    bot.send_media_group(message.chat.id, [
        types.InputMediaPhoto(photo1, caption="Вот твои улики, Супермен!"),
        types.InputMediaPhoto(photo2)
    ])

@bot.message_handler(commands=['ask'])
def ask_question(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "В каком городе нужна твоя помощь?", reply_markup=markup)

# Этот обработчик поймает любой ответ на сообщение выше
@bot.message_handler(func=lambda message: message.reply_to_message and "В каком городе" in message.reply_to_message.text)
def get_city(message):
    bot.reply_to(message, f"Принято! Вылетаю в {message.text}!")


    @bot.message_handler(func=lambda message: any(word in message.text.lower() for word in ['криптонит', 'зло', 'яд']))
def security_filter(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "⚠️ Сообщение удалено системой безопасности Метрополиса!")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "accept_mission":
        bot.answer_callback_query(call.id, "Миссия принята!") # Всплывашка сверху
        bot.edit_message_text("Статус: Выполняется... 🚀", call.message.chat.id, call.message.message_id)
    elif call.data == "decline_mission":
        bot.answer_callback_query(call.id, "Миссия отклонена", show_alert=True) # Окно с кнопкой ОК