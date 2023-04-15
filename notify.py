import telebot
import schedule
import time

# Создание бота с помощью токена
bot = telebot.TeleBot("6190642798:AAHDpVDtMlW5rlD4UY7cDMbLrcnWwUU4TqQ")

# Задание расписания для каждого сотрудника
schedule.every().day.at("17:00").do(lambda: bot.send_message(chat_id="ID_сотрудника_А", text="Отправить накладные клиентам"))
schedule.every().day.at("20:15").do(lambda: bot.send_message(chat_id="808629478", text="Проверить всех ли клиентов подключили к боту в телеграмм"))

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    # Отправляем приветственное сообщение
    bot.send_message(chat_id=message.chat.id, text="Привет, я бот для уведомлений о задачах!")
    # Отправляем уведомления каждому сотруднику в соответствии с его расписанием
    while True:
        schedule.run_pending()
        time.sleep(1)

# Запуск бота
bot.polling()


