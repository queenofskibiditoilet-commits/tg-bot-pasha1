Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import telebot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'telebot'
>>>
>>> # Замените 'ТВОЙ_ТОКЕН' на токен от BotFather
>>> TOKEN = 'ТВОЙ_ТОКЕН'
>>> bot = telebot.TeleBot(TOKEN)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'telebot' is not defined
>>>
>>> @bot.message_handler(commands=['start'])
... def send_welcome(message):
...     bot.reply_to(message, "Привет! Я работаю на бесплатном хостинге 24/7!")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> @bot.message_handler(func=lambda message: True)
... def echo_all(message):
...     bot.reply_to(message, message.text)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Запуск бота
>>> if __name__ == '__main__':
...     bot.infinity_polling()
... import os
  File "<stdin>", line 3
    import os
    ^^^^^^
SyntaxError: invalid syntax
>>> from flask import Flask, request
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'flask'
>>> import telebot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'telebot'
>>>
>>> # Вставьте ваш токен от BotFather
>>> TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER'
>>>
>>> bot = telebot.TeleBot(TOKEN)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'telebot' is not defined
>>> app = Flask(__name__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Flask' is not defined
>>>
>>> # Обработка команды /start
>>> @bot.message_handler(commands=['start'])
... def start(message):
...     bot.reply_to(message, "Привет! Я работаю на Vercel через Webhooks!")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Обработка текстовых сообщений
>>> @bot.message_handler(func=lambda message: True)
... def echo(message):
...     bot.reply_to(message, message.text)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Точка входа для Vercel (вебхук)
>>> @app.route('/', methods=['POST'])
... def webhook():
...     if request.headers.get('content-type') == 'application/json':
...         json_string = request.get_data().decode('utf-8')
...         update = telebot.types.Update.de_json(json_string)
...         bot.process_new_updates([update])
...         return ''
...     return 'Forbidden', 403
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>> # Проверка работоспособности в браузере
>>> @app.route('/', methods=['GET'])
... def index():
...     return "Bot is running!import os
  File "<stdin>", line 3
    return "Bot is running!import os
           ^
SyntaxError: unterminated string literal (detected at line 3)
>>> from flask import Flask, request
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'flask'
>>> import telebot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'telebot'
>>>
>>> # Вставьте ваш токен от BotFather
>>> TOKEN = 'ТВОЙ_ТОКЕН_ОТ_BOTFATHER'
>>>
>>> bot = telebot.TeleBot(TOKEN)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'telebot' is not defined
>>> app = Flask(__name__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Flask' is not defined
>>>
>>> # Обработка команды /start
>>> @bot.message_handler(commands=['start'])
... def start(message):
...     bot.reply_to(message, "Привет! Я работаю на Vercel через Webhooks!")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Обработка текстовых сообщений
>>> @bot.message_handler(func=lambda message: True)
... def echo(message):
...     bot.reply_to(message, message.text)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Точка входа для Vercel (вебхук)
>>> @app.route('/', methods=['POST'])
... def webhook():
...     if request.headers.get('content-type') == 'application/json':
...         json_string = request.get_data().decode('utf-8')
...         update = telebot.types.Update.de_json(json_string)
...         bot.process_new_updates([update])
...         return ''
...     return 'Forbidden', 403
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>> # Проверка работоспособности в браузере
>>> @app.route('/', methods=['GET'])
... def index():
...     return "Bot is import os
  File "<stdin>", line 3
    return "Bot is import os
           ^
SyntaxError: unterminated string literal (detected at line 3)
>>> from flask import Flask, request
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'flask'
>>> import telebot
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'telebot'
>>>
>>> # Вставьте ваш токен от BotFather
>>> TOKEN = '8731810948:AAExaK52-5FhxjzAy86lBxVg1j6UkjV-Z2o'
>>>
>>> bot = telebot.TeleBot(TOKEN)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'telebot' is not defined
>>> app = Flask(__name__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Flask' is not defined
>>>
>>> # Обработка команды /start
>>> @bot.message_handler(commands=['start'])
... def start(message):
...     bot.reply_to(message, "Привет! Я работаю на Vercel через Webhooks!")
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Обработка текстовых сообщений
>>> @bot.message_handler(func=lambda message: True)
... def echo(message):
...     bot.reply_to(message, message.text)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'bot' is not defined
>>> # Точка входа для Vercel (вебхук)
>>> @app.route('/', methods=['POST'])
... def webhook():
...     if request.headers.get('content-type') == 'application/json':
...         json_string = request.get_data().decode('utf-8')
...         update = telebot.types.Update.de_json(json_string)
...         bot.process_new_updates([update])
...         return ''
...     return 'Forbidden', 403
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'app' is not defined
>>> # Проверка работоспособности в браузере
>>> @app.route('/', methods=['GET'])
... def index():
...     return "Bot is running!"
