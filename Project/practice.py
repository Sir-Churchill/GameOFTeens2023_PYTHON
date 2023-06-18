import telebot
from telebot import types

bot = telebot.TeleBot('----')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Почати опитування')
    bot.send_message(message.chat.id, 'Вітаю, я бот від Lifecell, і моя задача - допомогти вам з вибором тарифу! '
                                      'Якщо готові, натисніть "Почати опитування"', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Почати опитування')
def start_survey(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Так', 'Ні')
    bot.send_message(message.chat.id, 'Ви бажаєте тариф для себе?', reply_markup=keyboard)
    bot.register_next_step_handler(message, question_1)

def question_1(message):
    if message.text == 'Так':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Так', 'Ні')
        bot.send_message(message.chat.id, 'Чи потрібен вам необмежений мобільний Інтернет?', reply_markup=keyboard)
        bot.register_next_step_handler(message, question_2)
    elif message.text == 'Ні':
        bot.send_message(message.chat.id, "Ви бажаєте тариф для сім'ї?")
        bot.register_next_step_handler(message, q1)

def question_2(message):
    if message.text == 'Так':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Так', 'Ні')
        bot.send_message(message.chat.id, 'Чи потрібно вам якомога більше хвилин для спілкування по телефону?', reply_markup=keyboard)
        bot.register_next_step_handler(message, suggest_package)
    elif message.text == 'Ні':
        bot.send_message(message.chat.id, 'Вам потрібен пакет з мінімальними послугами?')
        bot.register_next_step_handler(message, question_3)

def question_3(message):
    if message.text == 'Так':
        bot.send_message(message.chat.id, 'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/prosto-life-2021/')

    elif message.text == 'Ні':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/smart-life-2021/')
    back(message)

def q1(message):
    if message.text == 'Так':
        bot.send_message(message.chat.id, 'Ви бажаєте тариф для своєї дитини?')
        bot.register_next_step_handler(message, q2)
    elif message.text == 'Ні':
        bot.send_message(message.chat.id, "Ви бажаєте тариф для Ґаджетів?")
        bot.register_next_step_handler(message, q3)

def q2(message):
    if message.text == 'Так':
        bot.send_message(message.chat.id, 'Ми рекомендуємо для розляду такий тариф: \n https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/shkilniy/')
        back(message)
    elif message.text == 'Ні':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('S', 'M', 'L')
        bot.send_message(message.chat.id, "Можете обрати обсяг пакету S, M, L", reply_markup=keyboard)
        bot.register_next_step_handler(message, q5)

def q3(message):
    if message.text == 'Так':
        bot.send_message(message.chat.id, "Запропонуємо вам 3 різні пакети: Ґаджет Безпека, Ґаджет Смарт, Ґаджет Планшет, Ґаджет Роутер")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Ґаджет Безпека', 'Ґаджет Смарт', 'Ґаджет Планшет', 'Ґаджет Роутер')
        bot.send_message(message.chat.id, 'Виберіть один з пакетів:', reply_markup=keyboard)
        bot.register_next_step_handler(message, q4)
    if message.text == 'Ні':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add('Почати опитування')
        bot.register_next_step_handler(message, start_survey)
        bot.send_message(message.chat.id, 'Мабуть вам підійде щось інше, спробуйте ще', reply_markup=keyboard)


def q4(message):
    if message.text == 'Ґаджет Безпека':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-bezpeka/ ')
    elif message.text == 'Ґаджет Смарт':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-smart/ ')
    elif message.text == 'Ґаджет Планшет':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-planshet/')
    elif message.text == 'Ґаджет Роутер':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/gadget-router/' )
    back(message)

def q5(message):
    if message.text == 'S':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/paket-s/ \nДякуємо за вибір Lifecell')

    elif message.text == 'M':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/paket-m/ \nДякуємо за вибір Lifecell')

    elif message.text == 'L':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/paket-l/ \nДякуємо за вибір Lifecell')
    back(message)


def suggest_package(message):
    if message.text == 'Так':
        bot.send_message(message.chat.id, 'Тоді можемо запропонувати вам цей пакет:')
        bot.send_message(message.chat.id, 'https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/platinum-life-2021/')
    elif message.text == 'Ні':
        bot.send_message(message.chat.id,
                         'Ми рекомендуємо для розляду такий тариф: \nhttps://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/vilniy-life-2021/')
    back(message)

def back(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Почати опитування')
    bot.send_message(message.chat.id, 'Дякуємо за вибір нашої компанії, з повагою команда Lifecell',
                     reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Якщо бажаєте можете повторити опитування', reply_markup=keyboard)
    bot.register_next_step_handler(message, start_survey)

bot.infinity_polling()
