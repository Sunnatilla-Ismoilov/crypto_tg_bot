import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI

token = '5446673681:AAHUWmXc-sCmch1eMGH7G7Me_Y7NO6HYgk4'
cg = CoinGeckoAPI()



bot = telebot.TeleBot(token)
listt = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(str(listt))

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('BTC/USDT')
    item2 = types.KeyboardButton('ETH/USDT')
    item3 = types.KeyboardButton('ADA/USDT')
    info = types.KeyboardButton('Info')

    markup.add(item1, item2, item3, info)
    bot.send_message(message.chat.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Info':
            bot.send_message(message.chat.id, 'Этот бот поможет вам узнать цену самых топовых криптовалют')
        elif message.text == 'BTC/USDT':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Курс криптовалюты Bitcoin к USDT')
            back = types.KeyboardButton('Back')
            markup.add(item1, back)
            bot.send_message(message.chat.id, (f"BTC/USDT: {str(listt.get('usd'))}") , reply_markup=markup)
        elif message.text == 'Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('BTC/USDT')
            item2 = types.KeyboardButton('ETH/USDT')
            item3 = types.KeyboardButton('ADA/USDT')
            info = types.KeyboardButton('Info')

            markup.add(item1, item2, item3, info)
            bot.send_message(message.chat.id, 'Back' , reply_markup=markup)





bot.infinity_polling()