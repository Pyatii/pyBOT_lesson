token="your_token" #Ввод токена с GodFatherBot
import telebot #Импортирование библиотеки
passwords={"admin":"admin"} #Словарь с логинами и паролями
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
@bot.message_handler(commands=['authorize']) #Функция авторизации
def authorize(message):
    bot.send_message(message.chat.id, "Введите свой логин и пароль (логин:пароль")
    @bot.message_handler()
    def auth(new_message):
        txt=new_message.text.split(":") #Строка логин:пароль делится по двоеточию
        if txt[0] in passwords: #Если введеный логин есть в логинах, то
            if passwords[txt[0]] == txt[1]: #Если пароль соответствует нашему логину, то выводим сообщение об успешной авторизации
                bot.send_message(new_message.chat.id, "Вы авторизованы")
            else: bot.send_message(new_message.chat.id, "Неправильный пароль") #Если условие с соответствием пароля не выполнилось, то выводим сообщение об ошибке
        else: bot.send_message(new_message.chat.id, "Такого пользователя не существует") #Если логина не существует, то выводим сообщение об ошибке


bot.polling(none_stop=True) #Метод polling обрабатывает входящие event`ы (события), параметр none_stop отвечает за беспрерывную работу
