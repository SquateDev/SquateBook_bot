import telebot
from telebot import types

TOKEN = '8041209016:AAExfj3xkzk6GnvIwizuv2oyqrrRO5Fn_D0'
bot = telebot.TeleBot(TOKEN)

# Список запрещённых слов
profanities = ["шлюха", "шлю́ха", "хуй", "пидор", "пидорас", "инвалид", "еблан", "питух", "петух", "петушара", "сука", "нахуй", "на́ху́й", "сдохла", "конченый", "писю", "соси", "анёба", "айкю", "IQ", "iq", "конченая"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Помочь с читом")
    btn2 = types.KeyboardButton("Сделать чит")
    btn3 = types.KeyboardButton("Помочь Админу")
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, "Что вы хотите?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Помочь с читом", "Сделать чит"])
def handle_choice(message):
    bot.send_message(message.chat.id, "Напиши, чем помочь, и администратор напишет тебе в личку!")
    bot.register_next_step_handler(message, process_response)

def process_response(message):
    # Проверка на наличие мата
    if any(profanity in message.text.lower() for profanity in profanities):
        bot.send_message(message.chat.id, "Давайте, пожалуйста, без мата.")
        # Возвращаемся к ожиданию нового сообщения
        bot.register_next_step_handler(message, process_response)
        return
    
    user_id = 7095203663
    username = message.from_user.username if message.from_user.username else "Без юзернейма"
    bot.send_message(user_id, f"Сообщение от пользователя @{username} (ID: {user_id}): {message.text}")

@bot.message_handler(func=lambda message: message.text == "Помочь Админу")
def help_admin(message):
    bot.send_message(message.chat.id, "Вот ссылка для помощи: https://www.donationalerts.com/r/squate_dev")

bot.polling()
