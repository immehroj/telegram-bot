import random

from telebot import TeleBot, types

import config
import messages
import jokes


bot = TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, messages.start_message)


@bot.message_handler(commands=['help'])
def help_message(message: types.Message):
    bot.send_message(message.chat.id, messages.help_message)


@bot.message_handler(commands=['joke'])
def joke_message(message: types.Message):
    bot.send_message(message.chat.id, random.choice(jokes.KNOWN_JOKES))


@bot.message_handler()
def echo_message(message: types.Message):
    text = message.text
    if 'привет' in text.lower():
        text = 'И тебе привет!'
    elif 'как дела' in text.lower():
        text = 'Хорошо! А у вас как?'
    elif 'пока' in text.lower() or 'до свидания' in text.lower():
        text = 'До новых встреч!'
    bot.send_message(message.chat.id, text)


bot.infinity_polling(skip_pending=True)