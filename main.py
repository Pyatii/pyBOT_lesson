token="your_token" #Ввод токена с GodFatherBot
import telebot #Импортирование библиотеки
bot = telebot.TeleBot(token=token) #Авторизация через токен
@bot.message_handler(commands=['start']) #Декоратор для команды /start
def say_hi(message): #Функция, отвечающая на команду /start
    bot.send_message(message.chat.id, "Привет, пользователь!") #send_message - метод TelegramBotAPI, позволяющий общаться с пользователем bot.send_message(ID чата (integer), "Текст сообщения (string)")  
@bot.message_handler(commands=['calculate']) #Декоратор для команды /calculate
def calculate(message):
    bot.send_message(message.chat.id, "Введите мат. выражение")
    @bot.message_handler() #Декоратор для сообщений, поступающих после ввода команды /calculate
    def return_out(new_message):
        bot.send_message(new_message.chat.id, eval(new_message.text)) #Функция eval позволяет выполнять команды Python из строчных значений 


bot.polling(none_stop=True) #Метод polling обрабатывает входящие event`ы (события), параметр none_stop отвечает за беспрерывную работу
