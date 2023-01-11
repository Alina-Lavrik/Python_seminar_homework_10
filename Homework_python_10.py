import telebot
from datetime import datetime
from pycbrf import ExchangeRates


bot = telebot.TeleBot('5924736461:AAHyjUG9LH3WdWrY9SIPRAxScaXYx4GsqQE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    currency1 = telebot.types.KeyboardButton('USD')
    currency2 = telebot.types.KeyboardButton('EUR')
    markup.add(currency1, currency2)
    bot.send_message(chat_id=message.chat.id, text='<b>Hello! if you want to see exchange rates choose currency</b>', reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def message(message):
    message_okey = message.text.strip().lower()
   
    if message_okey in ['usd', 'eur']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f'<b>{message_okey.upper()} rate is {float(rates[message_okey.upper()].rate)}</b>', parse_mode='html')


bot.polling(none_stop=True)
