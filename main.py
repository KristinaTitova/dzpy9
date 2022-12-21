import telebot
bot = telebot.TeleBot('5650424674:AAGPs-FVez4B4ehEBoespe2-AzJEQ-CQndY')

from telebot import types
bot(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

bot(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Сайт компании', url='https://gb.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт GeekBrains", reply_markup = markup)

bot(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Как стать учеником?')
        btn2 = types.KeyboardButton('Оферта')
        btn3 = types.KeyboardButton('Программы')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)
    elif message.text == 'Как стать учеником?':
        bot.send_message(message.from_user.id, 'Вам нужно выбрать программу и оставить заявку. После с вами свяжутся ', parse_mode='Markdown')

    elif message.text == 'Оферта':
        bot.send_message(message.from_user.id, 'Прочитать оферту вы можете по ' + '[ссылке](https://gbcdn.mrgcdn.ru/uploads/staticpage/433/asset/8fbb901448467da351508b7a45493be7.pdf)', parse_mode='Markdown')
    elif message.text == 'Программы':
        bot.send_message(message.from_user.id, 'Выбрать программу вы можете по ' + '[ссылке](https://gb.ru/courses/all)', parse_mode='Markdown')

        bot.polling(none_stop=True, interval=0)