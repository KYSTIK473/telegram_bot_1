import telebot
from telebot import types

SCORE = 0
TYPE = None
bot = telebot.TeleBot('1714242320:AAF9f2rtL8BwKop-Fcet-cbdiTCMbXPMdt8')

ANSWERS = ['Новичок', 'От полугода до 1 года', 'От 1 года до 3х лет', 'От 3х до 5 лет', 'От 5 лет и более',
           'Консультацию',
           'Пакет сессий',
           'Коуч.Программа', 'Наставничество', 'Премиальная программа', '💰До 5 000р.', '🔺5 000-10 000р.',
           '🔹10 000-20 000р.',
           '🔸20 000-50 000р.',
           'От 50 000 руб. и выше', '🗣Сарафан', '📸Инстаграм', '💻Агрегаторы', '🏙ВК, Тг', '🤷‍♀️У меня нет клиентов',
           '3 - 5 разных типов', 'Абсолютно разные', 'Один тип с одинаковыми запросами',
           '😕1 клиент', '😐От 2 до 4', '😼От 5 до 7', '🙆‍♀️От 7', '🤷‍♀️Нет новых клиентов',
           '1 из 5', '2 из 5', '3 из 5', '4 из 5', '5 из 5',
           '✊500-2 000 руб.', '👍2 000-5 000 руб.', '👌5 000 - 15 000 руб.', '🥺Не вкладываю',
           'Вкладываю, но результат 0']
QUESTIONS = ["""1️⃣ Как давно ты работаешь в своем направлении?

👇Нажми на кнопку со своим вариантом""", """2️⃣ Когда к тебе обращается новый клиент, какой продукт 
ты ему предлагаешь?""", """3️⃣ Какую стоимость своего продукта ты озвучиваешь клиенту?""",
             """4️⃣ Откуда чаще всего к тебе приходит основная часть клиентов?""",
             """5️⃣ Какой тип клиентов приходит к тебе чаще всего?

Тип клиента, например: предприниматель

Запрос: хочет пробить стеклянный потолок в 100.000 рублей""", """6️⃣ Сколько у тебя новых клиентов в месяц?""", """7️⃣ Сколько клиентов ты закрываешь в оплачиваемую работу после бесплатной консультации?

Берем за норму 5 клиентов из 5 после консультации заходят в платную работу""",
             """8️⃣ Какой бюджет потратил на свое продвижение или поиск клиентов в прошлом месяце?"""]


@bot.message_handler(commands=['start'])
def start(message):
    msg = """, привет!🖐🏻

Я подготовил мини-тест из 8 вопросов, после которого узнаешь сможешь ли ты зарабатывать в новых реалиях 
БЕЗ ИНСТАГРАМА.

После прохождения теста ты получишь не только результаты, но и ценный подарок 🎁 Пошаговый план "Как сейчас выйти на стабильный доход от 200 000 р."

"""
    ph = open('photo1660130622.jpeg', 'rb')
    bot.send_photo(message.chat.id, ph)
    markup = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text='👍Давай', callback_data="test1")
    markup.add(switch_button)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}{msg}', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    global SCORE, TYPE, ANSWERS, QUESTIONS
    if call.message:
        if call.data == "test1":
            msg = """🙋‍♂️ Я, Александр Ганичев, наставник экспертов и коучей

Помог 8 клиентам заработать 3 120 000 рублей в первый месяц

Более 10 лет предприниматель. Мах оборот более 100 млн. руб. в год.
2 года в маркетинге. Генерировал “тёплых” клиентов.
В продюсировании сделал экспертам 5 и 1,5 млн. руб. за месяц.
С 2010 года тренер по продажам (обожаю обучать продажам).

Накинул совсем немного личных заслуг, чтобы у тебя сложилось обо мне небольшое представление.

И да, мне есть, чем поделиться с тобой 😉

Сильно твоё время полотнами текста о себе занимать не буду, поэтому летим дальше

👇Жми кнопку и продолжаем"""
            ph = open('photo1660130628.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text='👍Приятно познакомиться', callback_data="test2")
            markup.add(switch_button)
            bot.send_message(call.message.chat.id, f'{msg}', reply_markup=markup)
        elif call.data == 'test2':
            msg = """🔥Вдобавок к тесту я приготовил для тебя две мощных статьи на тему запуска своего продукта или услуги для коучей, экспертов и наставников, поэтому не убегай сразу.

            👨‍🎓В статьях я описал личный опыт и методы, проверенные моими доходами, временем и нервами, а также подготовил материал, в котором описал, как стать востребованным специалистом в 2022 году и иметь стабильный поток клиентов

            🎯Нужно выполнить лишь 5 пунктов, которые позволят выйти на желаемый доход.

            👌🏻100 % откроешь для себя новый мир!

            Ну или хотя бы почерпнешь ценного, например, как заработать 
            эксперту 360 000 ₽ за 20 дней =)

            Будет интересно, гарантирую😉

            👇Жми, чтобы продолжить

            *Чтобы ответить на вопрос теста нажимай на кнопку со своим вариантом ответа

            Только не торопись, бывает задержка до 1-2 секунды👇"""
            ph = open('photo1660207518.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text='✅Ок, ок!Где Тест?', callback_data="test3")
            markup.add(switch_button)
            bot.send_message(call.message.chat.id, f'{msg}', reply_markup=markup)
        elif call.data == 'test3':
            ph = open('photo1660207565.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup()
            switch_button = types.InlineKeyboardButton(text='🚀Старт', callback_data="test4")
            markup.add(switch_button)
            bot.send_message(call.message.chat.id, f'➡️Отлично, поехали!')
            bot.send_message(call.message.chat.id, f'3️⃣...')
            bot.send_message(call.message.chat.id, f'2️⃣..')
            bot.send_message(call.message.chat.id, f'1️⃣...', reply_markup=markup)
        elif call.data == 'test4':
            msg = """➡️ В каком направлении ты работаешь?

👇           выбери ниже свой ответ"""
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text='Эксперт', callback_data='test51')
            switch_button1 = types.InlineKeyboardButton(text='Коуч', callback_data='test52')
            switch_button2 = types.InlineKeyboardButton(text='Психолог', callback_data='test53')
            switch_button3 = types.InlineKeyboardButton(text='Другое', callback_data='test54')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3)
            bot.send_message(call.message.chat.id, f'{msg}', reply_markup=markup)
        elif call.data[0:5] == 'test5':
            TYPE = int(call.data[-1])
            ph = open('photo1660208297.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text=ANSWERS[0], callback_data='test60')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[1], callback_data='test62')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[2], callback_data='test64')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[3], callback_data='test66')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[4], callback_data='test68')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[0]}', reply_markup=markup)
        elif call.data[0:5] == 'test6':
            SCORE += int(call.data[-1])
            ph = open('photo1660212901.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[0]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2]}")
            switch_button = types.InlineKeyboardButton(text=ANSWERS[5], callback_data='test70')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[6], callback_data='test72')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[7], callback_data='test74')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[8], callback_data='test76')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[9], callback_data='test78')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[1]}', reply_markup=markup)
        elif call.data[0:5] == 'test7':
            SCORE += int(call.data[-1])
            ph = open('photo1660212909.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[1]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 5]}")
            switch_button = types.InlineKeyboardButton(text=ANSWERS[10], callback_data='test80')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[11], callback_data='test82')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[12], callback_data='test84')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[13], callback_data='test86')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[14], callback_data='test88')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[2]}', reply_markup=markup)
        elif call.data[0:5] == 'test8':
            SCORE += int(call.data[-1])
            ph = open('photo1660214186.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[2]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 10]}")
            switch_button = types.InlineKeyboardButton(text=ANSWERS[15], callback_data='test90')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[16], callback_data='test92')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[17], callback_data='test94')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[18], callback_data='test96')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[19], callback_data='test98')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[3]}', reply_markup=markup)
        elif call.data[0:5] == 'test9':
            SCORE += int(call.data[-1])
            ph = open('photo1660214240.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[3]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 15]}")
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[20], callback_data='test104')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[21], callback_data='test106')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[22], callback_data='test108')
            markup.add(switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[4]}', reply_markup=markup)
        elif call.data[0:6] == 'test10':
            SCORE += int(call.data[-1])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[4]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 18]}")
            ph = open('photo1660214319.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text=ANSWERS[23], callback_data='test110')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[24], callback_data='test112')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[25], callback_data='test114')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[26], callback_data='test116')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[27], callback_data='test118')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[5]}', reply_markup=markup)
        elif call.data[0:6] == 'test11':
            SCORE += int(call.data[-1])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[5]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 23]}")
            ph = open('photo1660214384.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text=ANSWERS[28], callback_data='test120')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[29], callback_data='test122')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[30], callback_data='test124')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[31], callback_data='test126')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[32], callback_data='test128')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[6]}', reply_markup=markup)
        elif call.data[0:6] == 'test12':
            SCORE += int(call.data[-1])
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=f"{QUESTIONS[6]}\n\n"
                                       f"Вы выбрали: {ANSWERS[int(call.data[-1]) // 2 + 28]}")
            ph = open('photo1660214426.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text=ANSWERS[33], callback_data='test132')
            switch_button1 = types.InlineKeyboardButton(text=ANSWERS[34], callback_data='test134')
            switch_button2 = types.InlineKeyboardButton(text=ANSWERS[35], callback_data='test136')
            switch_button3 = types.InlineKeyboardButton(text=ANSWERS[36], callback_data='test138')
            switch_button4 = types.InlineKeyboardButton(text=ANSWERS[37], callback_data='test130')
            markup.add(switch_button, switch_button1, switch_button2, switch_button3, switch_button4)
            bot.send_message(call.message.chat.id, f'{QUESTIONS[7]}', reply_markup=markup)
        elif call.data[0:6] == 'test13':
            SCORE += int(call.data[-1])
            msg = f"""Поздравляю, ты успешно завершил тест!

Твое количество баллов: 50 из 64!

👇Нажми кнопку ниже и узнай, что означает это количество баллов"""
            bot.send_message(call.message.chat.id, f'Проверяю ответы...')
            bot.send_message(call.message.chat.id, f'3️⃣...')
            bot.send_message(call.message.chat.id, f'2️⃣...')
            bot.send_message(call.message.chat.id, f'1️⃣...')
            ph = open('photo1660214491.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text='👉Узанть', callback_data='test14')
            markup.add(switch_button)
            bot.send_message(call.message.chat.id, msg, reply_markup=markup)
        elif call.data[0:6] == 'test14':
            msg = f"""😉{call.message.chat.first_name}, вау! Отличный результат! У тебя максимальный потенциал для выхода на 200 000 рублей за счет своего продукта или услуги!

🏆Твоя готовность к запуску продаж своего продукта на 200 000 рублей МАКСИМАЛЬНАЯ!

Тебе срочно нужно запускать продажи, иначе мир клиентов без такого эксперта совсем не справится! 😏

"""
            bot.send_message(call.message.chat.id, msg)
            ph = open('photo1660215561.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, ph)
            markup = types.InlineKeyboardMarkup(row_width=2)
            switch_button = types.InlineKeyboardButton(text='🔥Читать статью', url="https://ya.ru")
            markup.add(switch_button)
            msg = """⚡️И да, так как баллов ты набрал большое количество. Специально для тебя подготовил материал, в котором описал, как в новых реалиях стать востребованным специалистом и иметь стабильный поток клиентов в 2022 году.

🎯Нужно выполнить лишь 5 пунктов, которые позволят выйти на желаемый доход.

👉В статье ты найдешь специальное предложение от меня, которое будет тебе максимально полезно!

👇Жми на кнопку и читай статью."""
            bot.send_message(call.message.chat.id, msg, reply_markup=markup)


bot.polling(non_stop=True)
