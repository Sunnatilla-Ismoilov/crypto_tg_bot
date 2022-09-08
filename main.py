import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
token = 'YOUR_TELEGRAM_BOT_API'
cg = CoinGeckoAPI()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('BTC/USDT')
    item2 = types.KeyboardButton('ETH/USDT')
    item3 = types.KeyboardButton('ADA/USDT')
    contacts = types.KeyboardButton('Контакты')

    markup.add(item1, item2, item3, contacts)
    bot.send_message(message.chat.id, 'Привет {0.first_name}!\n\nЭтот бот поможет узнать курс криптовалют по отношению к доллару!\n\nНиже выбери необходимую криптовалюту, чтобы узнать курс:'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Контакты':
            bot.send_message(message.chat.id, 'Этот бот был создан для информационных целей\n\nСоздателем этого ботя является: @Sunnatilla_Ismoilov')
        elif message.text == 'BTC/USDT':
            btc = cg.get_price(ids='bitcoin', vs_currencies='usd')
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, (f'BTC/USDT: {btc}') , reply_markup=markup)
        elif message.text == 'ETH/USDT':
            eth = cg.get_price(ids='ethereum', vs_currencies='usd')
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, (f'ETH/USDT: {eth}') , reply_markup=markup)
        elif message.text == 'ADA/USDT':
            ada = cg.get_price(ids='cardano', vs_currencies='usd')
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, (f'ADA/USDT: {ada}') , reply_markup=markup)
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('BTC/USDT')
            item2 = types.KeyboardButton('ETH/USDT')
            item3 = types.KeyboardButton('ADA/USDT')
            contacts = types.KeyboardButton('Контакты')

            markup.add(item1, item2, item3, contacts)
            bot.send_message(message.chat.id, 'Назад' , reply_markup=markup)





bot.infinity_polling()
