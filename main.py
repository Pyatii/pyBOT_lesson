token="your_token"
import telebot
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, "Привет, пользователь!")
@bot.message_handler(commands=['calculate'])
def calculate(message):
    bot.send_message(message.chat.id, "Введите мат. выражение")
    @bot.message_handler()
    def return_out(new_message):
        bot.send_message(new_message.chat.id, eval(new_message.text))


bot.polling(none_stop=True)
