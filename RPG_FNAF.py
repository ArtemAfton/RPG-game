import telebot
from telebot import types
from data_rpg import load_user_data_rpg, save_user_data_rpg
#from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from sujet_rpg import content
import time


token = "Your Token"

bot = telebot.TeleBot(token)

data_path_rpg = "user_data_rpg.json"
user_data_rpg = load_user_data_rpg(data_path_rpg)

def yes_start(message):
    if(message.text == "Да❗❗❗"):
        return "Да❗❗❗" in message.text

def where_am_i(message):
    if(message.text == "Где я?"):
        return "Где я?" in message.text

def who_are_you(message):
    if(message.text == "Кто ты?"):
        return "Кто ты?" in message.text

def am__i_die(message):
    if(message.text == "То есть, я умер?"):
        return "То есть, я умер?" in message.text

def is_he_purple(message):
    if(message.text == "Он реально фиолетовый?"):
        return "Он реально фиолетовый?" in message.text

def especially_me(message):
    if(message.text == "Именно моя?"):
        return "Именно моя?" in message.text

def i_want_home(message):
    if(message.text == "Я хочу домой"):
        return "Я хочу домой" in message.text

def is_this_dream(message):
    if(message.text == "Это всё похоже на сон..."):
        return "Это всё похоже на сон..." in message.text

def i_will_try(message):
    if(message.text == "Что ж, я попробую"):
        return "Что ж, я попробую" in message.text

def if_i_dont_want(message):
    if(message.text == "А если я не хочу?"):
        return "А если я не хочу?" in message.text

def go_away(message):
    if(message.text == "Уйти"):
        return "Уйти" in message.text

def help(message):
    if(message.text == "Помогу"):
        return "Помогу" in message.text

def one_of_whom(message):
    if(message.text == "Одним из кого?"):
        return "Одним из кого?" in message.text

def yes(message):
    if(message.text == "Да"):
        return "Да" in message.text

def heroo(message):
    if(message.text == "Фредди" or message.text == "Фокси" or message.text == "Бонни" or message.text == "Чика"):
        return  "Фредди" or  "Фокси" or  "Бонни" or  "Чика" in message.text

def thank_you(message):
    if(message.text == "Поблагодарить"):
        return "Поблагодарить" in message.text

def nope(message):
    if(message.text == "нет"):
        return "нет" in message.text

def if_i_loose(message):
    if(message.text == "А если я не справлюсь?"):
        return "А если я не справлюсь?" in message.text

def what_a_(message):
    if(message.text == "Какой-то бред"):
        return "Какой-то бред" in message.text

def play(message):
    if(message.text == "Играть"):
        return "Играть" in message.text

def go_to_him(message):
    if(message.text == "Пойти к нему"):
        return "Пойти к нему" in message.text

def scream_help(message):
    if(message.text == "Звать на помощь"):
        return "Звать на помощь" in message.text

def play_again(message):
    if(message.text == "Играть снова"):
        return "Играть снова" in message.text

def try_escape(message):
    if(message.text == "Пытаться подняться"):
        return "Пытаться подняться" in message.text

def sometimes_better(message):
    if(message.text == "-Бывало лучше"):
        return "-Бывало лучше" in message.text

def why_you_interested(message):
    if(message.text == "-Какая тебе разница?"):
        return "-Какая тебе разница?" in message.text

def sorry(message):
    if(message.text == "-Прости"):
        return "-Прости" in message.text

def who_are_you2(message):
    if(message.text == "-Кто ты?"):
        return "-Кто ты?" in message.text

def to_know_how_it_calls(message):
    if(message.text == "-Знать бы как что у вас тут называется."):
        return "-Знать бы как что у вас тут называется." in message.text

def you_like_mexican(message):
    if(message.text == "-А ещё ты прирождённый мексиканец, хах."):
        return "-А ещё ты прирождённый мексиканец, хах." in message.text

def thank_you2(message):
    if(message.text == "поблагодарить"):
        return "поблагодарить" in message.text

def ask(message):
    if(message.text == "Спросить"):
        return "Спросить" in message.text

def glitchs(message):
    if(message.text == "Спросить про помехи"):
        return "Спросить про помехи" in message.text

def yellow_rabbit(message):
    if(message.text == "Спросить про кролика"):
        return "Спросить про кролика" in message.text

def golden_freddy(message):
    if(message.text == "Спросить про Голдена Фредди"):
        return "Спросить про Голдена Фредди" in message.text

def yellow_rabbit2(message):
    if(message.text == "-Жёлтого кролика?"):
        return "-Жёлтого кролика?" in message.text

def pay_attention(message):
    if(message.text == "Заметить"):
        return "Заметить" in message.text

def shhh(message):
    if(message.text == "Промолчать"):
        return "Промолчать" in message.text

def tell_about_puppet(message):
    if(message.text == "Спросить про Марионетку"):
        return "Спросить про Марионетку" in message.text

def what_goldenfreddy_do(message):
    if(message.text == "-Что тогда делает Голден Фредди в обычное время?"):
        return "-Что тогда делает Голден Фредди в обычное время?" in message.text

def what_incident(message):
    if(message.text == "-Какой инцидент?"):
        return "-Какой инцидент?" in message.text

def what_incidents(message):
    if(message.text == "-Что за неприятности?"):
        return "-Что за неприятности?" in message.text

def to_tell(message):
    if(message.text == "Рассказать"):
        return "Рассказать" in message.text

def back_to_start(message):
    if(message.text == "Вернуться в начало"):
        return "Вернуться в начало" in message.text

def hold_back(message):
    if(message.text == "Сдержаться"):
        return "Сдержаться" in message.text

def stay(message):
    if(message.text == "Остаться"):
        return "Остаться" in message.text

def first_variant(message):
    if(message.text == "Первый вариант"):
        return "Первый вариант" in message.text

def second_variant(message):
    if(message.text == "Второй вариант"):
        return "Второй вариант" in message.text

def play_again2(message):
    if(message.text == 'играть снова'):
        return 'играть снова' in message.text

def why_you_interested_2(message):
    if(message.text == 'Зачем тебе знать?'):
        return 'Зачем тебе знать?' in message.text

def me_me(message):
    if(message.text == f'Я {user_data_rpg[message.chat.id]["hero"]}'):
        return f'Я {user_data_rpg[message.chat.id]["hero"]}' in message.text

def details(message):
    if(message.text == "Детали?"):
        return "Детали?" in message.text

def for_what(message):
    if(message.text == "Для чего?"):
        return "Для чего?" in message.text

def come_with_them(message):
    if(message.text == "Пойти"):
        return "Пойти" in message.text

def delay(message):
    if(message.text == "Отказаться"):
        return "Отказаться" in message.text

def third_variant(message):
    if(message.text == "Третий вариант"):
        return "Третий вариант" in message.text

def play_2(message):
    if(message.text == "играть"):
        return "играть" in message.text


#@bot.message_handler(func=lambda message: message.text in ["Да❗❗❗"])
#bot.message_handler(func=lambda message: message.text in ["Где я?"])

#def make_keyboard(buttons):
    #keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    #for ell in buttons:
        #keyboard.add(KeyboardButton(ell))

    #return keyboard


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="FNAF: Overthrow", callback_data="button1")
    keyboard.add(button1)
    global user_data_rpg
    user_data_rpg[message.chat.id] = {"name": message.from_user.full_name,
                                      "hero": "",
                                      "level": "",
                                      "choice": ""}
    save_user_data_rpg(user_data_rpg, data_path_rpg)
    bot.send_message(message.chat.id, f"Добро пожаловать в РПГ-игру 'FNAF: The Birth of a Legend', {user_data_rpg[message.chat.id]['name']}! "
                     "Игра разделена на несколько частей, каждая из которых содержит свой сюжет. Ниже приведён список  список этих частей, "
                     "выбери, с какой части хочешь начать:\n P.S. игра находится в разработке, поэтому список пока неполный. "
                     "Приносим свои извенения! ", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да❗❗❗")
    btn2 = types.KeyboardButton("Нет 😢")
    markup.add(btn1, btn2)
    if call.data == "button1":
        photo1 = open("Glitchtrap1.jpg", "rb")
        photo2 = open("Glitchtrap2.jpg", "rb")
        photo3 = open("Glitchtrap3.jpg", "rb")
        photo4 = open("Glithtrap4.jpg", "rb")
        bot.send_message(call.message.chat.id, "Ты выбрал часть: FNAF: Overtrhrow. Идёт подготовка к игре...")
        time.sleep(5)
        bot.send_photo(call.message.chat.id, photo1, "Подготовка персонажей... 732BSDI^@%*JSC_ERROR____Glitch_tape1")
        time.sleep(5)
        bot.send_photo(call.message.chat.id, photo2,"Подключение ИИ... ETDYDYYXHEEEEEEEEEEEEEEEEERRRROR*********Glitch_tape2")
        time.sleep(5)
        bot.send_photo(call.message.chat.id, photo3,"Загрузка виртуального пространства... E53237bgsych/ERROR_-Glitch_tape999999999999999999")
        time.sleep(5)
        bot.send_photo(call.message.chat.id, photo4,f"GLITCHTRAP_UPLOADED_TO {user_data_rpg[call.message.chat.id]['name']}\n"
                                               "Скорее станьте героем этого мира FNAF!!!\n "
                                                    "Вы готовы?", reply_markup=markup)
        photo1.close()
        photo2.close()
        photo3.close()
        photo4.close()

@bot.message_handler(content_types=["text"], func=yes_start)
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Где я?")
    bt2 = types.KeyboardButton("Кто ты?")
    markup.add(bt1, bt2)
    with open("Start_game.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption=content["location1"]["text1"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=where_am_i)
def where__am_i(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bn1 = types.KeyboardButton("То есть, я умер?")
    bn2 = types.KeyboardButton("Кто ты?")
    bn3 = types.KeyboardButton("Он реально фиолетовый?")
    markup.add(bn1, bn2, bn3)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text2"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=who_are_you)
def who__are_you(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bnt1 = types.KeyboardButton("То есть, я умер?")
    bnt2 = types.KeyboardButton("Где я?")
    bnt3 = types.KeyboardButton("Он реально фиолетовый?")
    markup.add(bnt1, bnt2, bnt3)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text3"], reply_markup=markup)


@bot.message_handler(content_types=["text"], func=am__i_die)
def am_i_die(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Именно моя?")
    btn2 = types.KeyboardButton("Я хочу домой")
    btn3 = types.KeyboardButton("Это всё похоже на сон...")
    markup.add(btn1, btn2, btn3)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text4"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=is_he_purple)
def is_he_purple(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Именно моя?")
    btn2 = types.KeyboardButton("Я хочу домой")
    btn3 = types.KeyboardButton("Это всё похоже на сон...")
    markup.add(btn1, btn2, btn3)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text5"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=especially_me)
def especially__me(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Что ж, я попробую")
    bttn2 = types.KeyboardButton("А если я не хочу?")
    markup.add(bttn1, bttn2)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text6"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=i_want_home)
def i__want_home(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Что ж, я попробую")
    bttn2 = types.KeyboardButton("А если я не хочу?")
    bttn3 = types.KeyboardButton("Одним из кого?")
    markup.add(bttn1, bttn2, bttn3)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text7"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=is_this_dream)
def is__this_dream(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Что ж, я попробую")
    bttn2 = types.KeyboardButton("А если я не хочу?")
    markup.add(bttn1, bttn2)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text8"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=i_will_try)
def i__will_try(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bk1 = types.KeyboardButton("Фредди")
    bk2 = types.KeyboardButton("Фокси")
    bk3 = types.KeyboardButton("Бонни")
    bk4 = types.KeyboardButton("Чика")
    markup.add(bk1, bk2, bk3, bk4)
    with open("Golden_Freddy.jpg", "rb") as photo:
     bot.send_photo(message.chat.id, photo, content["location1"]["text9"], reply_markup=markup)
    bot.send_message(message.chat.id, content["location1"]["heroes"], reply_markup=markup)
    bot.send_message(message.chat.id, content["location1"]["text10"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=if_i_dont_want)
def if__i_dont_want(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bb1 = types.KeyboardButton("Уйти")
    bb2 = types.KeyboardButton("Помогу")
    markup.add(bb1, bb2)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location1"]["text11"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=go_away)
def go__away(message):
    bot.send_message(message.chat.id, content["location1"]["text12"], reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(content_types=["text"], func=help)
def i__will_try(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bk1 = types.KeyboardButton("Фредди")
    bk2 = types.KeyboardButton("Фокси")
    bk3 = types.KeyboardButton("Бонни")
    bk4 = types.KeyboardButton("Чика")
    markup.add(bk1, bk2, bk3, bk4)
    bot.send_message(message.chat.id, content["location1"]["text9"])
    time.sleep(3)
    bot.send_message(message.chat.id, content["location1"]["heroes"])
    time.sleep(3)
    bot.send_message(message.chat.id, content["location1"]["text10"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=one_of_whom)
def one__of_whom(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bttn1 = types.KeyboardButton("Что ж, я попробую")
    bttn2 = types.KeyboardButton("А если я не хочу?")
    markup.add(bttn1, bttn2)
    with open("Golden_Freddy.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, "Голден Фредди предпочёл молчание...", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=yes)
def yes_(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bnn1 = types.KeyboardButton("Поблагодарить")
    bnn2 = types.KeyboardButton("А если я не справлюсь?")
    bnn3 = types.KeyboardButton("Какой-то бред")
    markup.add(bnn1, bnn2, bnn3)
    with open("Golden_Freddy.jpg", "rb") as photo:
     bot.send_photo(message.chat.id, photo, content["location1"]["text13"], reply_markup=markup)


@bot.message_handler(content_types=["text"], func=heroo)
def hero_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bbn1 = types.KeyboardButton("Да")
    bbn2 = types.KeyboardButton("нет")
    markup.add(bbn1, bbn2)
    user_data_rpg[message.chat.id]["hero"] = message.text
    if message.text == "Фредди" or message.text == "Фокси" or message.text == "Бонни" or message.text == "Чика":
        save_user_data_rpg(user_data_rpg, data_path_rpg)
        bot.send_message(message.chat.id, f'Ты выбрал аниматроника {user_data_rpg[message.chat.id]["hero"]}.\n'
                                          f'Ты уверен в своём выборе?', reply_markup=markup)


@bot.message_handler(content_types=["text"], func=thank_you)
def thank__you(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("Играть")
    markup.add(b1)
    photo1_0 = open("Helpi.jpg", "rb")
    bot.send_message(message.chat.id, content["location1"]["text14"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! '
                                      'Вы только что прошли первый уровень FNAF:Overthrow! Совсем скоро вы перейдёте на следующий! '
                                      'Только потерпите немного :)')
    photo1_0.close()
    photo1_0 = open("Helpi.jpg", "rb")
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! Компания '
                                              'Fazbear Ent. одобрила вам переход на второй уровень! Скорее продолжайте играть!', reply_markup=markup)
    photo1_0.close()

@bot.message_handler(content_types=["text"], func=if_i_loose)
def if__i_loose(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("Играть")
    markup.add(b1)
    photo1_0 = open("Helpi.jpg", "rb")
    bot.send_message(message.chat.id, content["location1"]["text15"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! '
                                      'Вы только что прошли первый уровень FNAF:Overthrow! Совсем скоро вы перейдёте на следующий! '
                                      'Только потерпите немного :)')
    photo1_0.close()
    photo1_0 = open("Helpi.jpg", "rb")
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! Компания '
                                              'Fazbear Ent. одобрила вам переход на второй уровень! Скорее продолжайте играть!', reply_markup=markup)
    photo1_0.close()

@bot.message_handler(content_types=["text"], func=nope)
def no_pe(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bk1 = types.KeyboardButton("Фредди")
    bk2 = types.KeyboardButton("Фокси")
    bk3 = types.KeyboardButton("Бонни")
    bk4 = types.KeyboardButton("Чика")
    markup.add(bk1, bk2, bk3, bk4)
    bot.send_message(message.chat.id, content["location1"]["text9"], reply_markup=markup)
    bot.send_message(message.chat.id, content["location1"]["heroes"], reply_markup=markup)
    bot.send_message(message.chat.id, content["location1"]["text10"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=what_a_)
def what__a(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("Играть")
    markup.add(b1)
    photo1_0 = open("Helpi.jpg", "rb")
    bot.send_message(message.chat.id, content["location1"]["text16"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! '
                                              'Вы только что прошли первый уровень FNAF:Overthrow! Совсем скоро вы перейдёте на следующий! '
                                              'Только потерпите немного :)')
    photo1_0.close()
    photo1_0 = open("Helpi.jpg", "rb")
    time.sleep(10)
    bot.send_photo(message.chat.id, photo1_0, f'Поздравляю вас, {user_data_rpg[message.chat.id]["name"]}! Компания '
                                              'Fazbear Ent. одобрила вам переход на второй уровень! Скорее продолжайте играть!', reply_markup=markup)
    photo1_0.close()

@bot.message_handler(content_types=["text"], func=play)
def plaay(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bp1 = types.KeyboardButton("Пойти к нему")
    bp2 = types.KeyboardButton("Остаться")
    markup.add(bp1, bp2)
    bot.send_message(message.chat.id, content["location2"]["text1"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=go_to_him)
def go__to_him(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kk1 = types.KeyboardButton("Звать на помощь")
    kk2 = types.KeyboardButton("Пытаться подняться")
    markup.add(kk1, kk2)
    bot.send_message(message.chat.id, content["location2"]["text2"], reply_markup=types.ReplyKeyboardRemove())
    with open("Mountains.mp4", "rb") as video:
        time.sleep(10)
        bot.send_video(message.chat.id, video, caption=content["location2"]["text3"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=scream_help)
def scream__help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp1 = types.KeyboardButton("Играть снова")
    markup.add(pp1)
    bot.send_message(message.chat.id, content["location2"]["text4"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=play_again)
def play__again(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bp1 = types.KeyboardButton("Пойти к нему")
    bp2 = types.KeyboardButton("Остаться")
    markup.add(bp1, bp2)
    bot.send_message(message.chat.id, content["location2"]["text1"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=try_escape)
def try__escape(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp3 = types.KeyboardButton("-Бывало лучше")
    pp2 = types.KeyboardButton("-Какая тебе разница?")
    markup.add(pp3, pp2)
    bot.send_message(message.chat.id, content["location2"]["text5"], reply_markup=types.ReplyKeyboardRemove())
    with open("El_Chip.jpg", "rb") as photo:
        time.sleep(5)
        bot.send_photo(message.chat.id, photo, "-Ну как ты, приятель?-спросил он.", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=sometimes_better)
def sometimes__better(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp7 = types.KeyboardButton("-Кто ты?")
    markup.add(pp7)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo,"-Понятно.", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=why_you_interested)
def why__you_interested(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp8 = types.KeyboardButton("-Прости")
    markup.add(pp8)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, "-Просто поинтересовался. Смотрю ты не слишком вежлив.", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=sorry)
def sor_ry(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pp7 = types.KeyboardButton("-Кто ты?")
    markup.add(pp7)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo,"Незнакомец кивнул.", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=who_are_you2)
def who_are_you_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl1 = types.KeyboardButton("-Знать бы как что у вас тут называется.")
    kl2 = types.KeyboardButton("-А ещё ты прирождённый мексиканец, хах.")
    markup.add(kl1, kl2)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text6"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=to_know_how_it_calls)
def to__know_how_it_calls(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl5 = types.KeyboardButton("поблагодарить")
    markup.add(kl5)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text7"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=you_like_mexican)
def you__like_mexican(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl3 = types.KeyboardButton("Спросить")
    kl4 = types.KeyboardButton("Сдержаться")
    markup.add(kl3, kl4)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text8"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=thank_you2)
def thank__you2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl3 = types.KeyboardButton("Спросить")
    kl4 = types.KeyboardButton("Сдержаться")
    markup.add(kl3, kl4)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text9"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=ask)
def a_s_k(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl6 = types.KeyboardButton("Спросить про помехи")
    kl7 = types.KeyboardButton("Спросить про кролика")
    kl8 = types.KeyboardButton("Спросить про Голдена Фредди")
    markup.add(kl6, kl7, kl8)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text10"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=glitchs)
def glitches(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl9 = types.KeyboardButton("-Жёлтого кролика?")
    markup.add(kl9)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text11"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=yellow_rabbit)
def yellow__rabbit(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl10 = types.KeyboardButton("Заметить")
    kl11 = types.KeyboardButton("Промолчать")
    markup.add(kl10, kl11)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text12"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=golden_freddy)
def golden__freddy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl11 = types.KeyboardButton("Спросить про Марионетку")
    kl12 = types.KeyboardButton("-Какой инцидент?")
    markup.add(kl11, kl12)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text13"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=yellow_rabbit2)
def yellow__rabit2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl13 = types.KeyboardButton("Рассказать")
    kl14 = types.KeyboardButton("сдержаться")
    markup.add(kl13, kl14)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo,"-Ну типо...А как ты узнал?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=pay_attention)
def pay__attention(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text14"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=shhh)
def shhhhhh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text15"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=tell_about_puppet)
def tell__about_puppet(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl16 = types.KeyboardButton("-Что тогда делает Голден Фредди в обычное время?")
    kl17 = types.KeyboardButton("-Что за неприятности?")
    markup.add(kl16, kl17)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text16"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=what_goldenfreddy_do)
def what__goldenfreddy_do(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text18"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=what_incident)
def what__incident(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text17"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=what_incidents)
def what__incidents(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text18"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=to_tell)
def to__tell(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    with open("El_Chip.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, content["location2"]["text19"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=hold_back)
def hold__back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kl15 = types.KeyboardButton("Вернуться в начало")
    markup.add(kl15)
    bot.send_message(message.chat.id, content["location2"]["text22"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=stay)
def sta__y(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ck1 = types.KeyboardButton("Первый вариант")
    ck2 = types.KeyboardButton("Второй вариант")
    ck3 = types.KeyboardButton("Третий вариант")
    markup.add(ck1, ck2, ck3)
    bot.send_message(message.chat.id, content["location2"]["text23"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    bot.send_message(message.chat.id, "'Первый или третий'-услышали вы, но никого рядом не было.")
    time.sleep(5)
    with open("Dark_forest.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Первый - через тёмный лес.")
    time.sleep(5)
    with open("River.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Второй- через бурную реку.")
    time.sleep(5)
    with open("Mountains2.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Третий- через скалистые холмы.")
    bot.send_message(message.chat.id, "Выбор за вами!\n"
                                      "P.S. Помните! Только двое путей ведут в правильное место, а один - в гибель!",
                     reply_markup=markup)

@bot.message_handler(content_types=["text"], func=back_to_start)
def back__to_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ck1 = types.KeyboardButton("Первый вариант")
    ck2 = types.KeyboardButton("Второй вариант")
    ck3 = types.KeyboardButton("Третий вариант")
    markup.add(ck1, ck2, ck3)
    with open("Start_game.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption=content["location2"]["text20"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    bot.send_message(message.chat.id, content["location2"]["text21"])
    time.sleep(20)
    bot.send_message(message.chat.id, "'Первый или третий'-услышали вы, но никого рядом не было.")
    time.sleep(5)
    with open("Dark_forest.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Первый - через тёмный лес.")
    time.sleep(5)
    with open("River.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Второй- через бурную реку.")
    time.sleep(5)
    with open("Mountains2.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Третий- через скалистые холмы.")
    bot.send_message(message.chat.id, "Выбор за вами!\n"
                                      "P.S. Помните! Только двое путей ведут в правильное место, а один - в гибель!", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=first_variant)
def first__variant(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu1 = types.KeyboardButton(f'Я {user_data_rpg[message.chat.id]["hero"]}')
    yu2 = types.KeyboardButton('Зачем тебе знать?')
    markup.add(yu1, yu2)
    bot.send_message(message.chat.id, content["location2"]["text24"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    with open("Pizzeria.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="Заброшенная пиццерия? 'Выглядит криповенько...'-подумали вы.")
    time.sleep(15)
    bot.send_message(message.chat.id,  content["location2"]["text25"])
    with open("Animatronics2.jpg", "rb") as photo:
        time.sleep(15)
        bot.send_photo(message.chat.id, photo, caption="Четырёх сломанных аниматроников...Лиса, Медведь, Кролик и Курица..."
                                                       "Вероятно они когда-то были талисманами "
                                                       "данной пиццерии.")
    time.sleep(5)
    bot.send_message(message.chat.id, content["location2"]["text26"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=second_variant)
def second__variant(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu3 = types.KeyboardButton('играть снова')
    markup.add(yu3)
    bot.send_message(message.chat.id, content["location2"]["text27"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=play_again2)
def play__again2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ck1 = types.KeyboardButton("Первый вариант")
    ck2 = types.KeyboardButton("Второй вариант")
    ck3 = types.KeyboardButton("Третий вариант")
    markup.add(ck1, ck2, ck3)
    with open("Start_game.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption=content["location2"]["text20"],
                       reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    bot.send_message(message.chat.id, content["location2"]["text21"])
    time.sleep(20)
    bot.send_message(message.chat.id, "'Первый или третий'-услышали вы, но никого рядом не было.")
    time.sleep(5)
    with open("Dark_forest.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Первый - через тёмный лес.")
    time.sleep(5)
    with open("River.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Второй- через бурную реку.")
    time.sleep(5)
    with open("Mountains2.mp4", "rb") as video:
        bot.send_video(message.chat.id, video, caption="Третий- через скалистые холмы.")
    bot.send_message(message.chat.id, "Выбор за вами!\n"
                                      "P.S. Помните! Только двое путей ведут в правильное место, а один - в гибель!",
                     reply_markup=markup)

@bot.message_handler(content_types=["text"], func=me_me)
def me__me(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu4 = types.KeyboardButton("Детали?")
    yu5 = types.KeyboardButton("Для чего?")
    markup.add(yu4, yu5)
    bot.send_message(message.chat.id, content["location2"]["text28"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=why_you_interested_2)
def why__you_interested_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu1 = types.KeyboardButton(f'Я {user_data_rpg[message.chat.id]["hero"]}')
    markup.add(yu1)
    bot.send_message(message.chat.id, "-А как я по-твоему пойму, ты ли тот кого имел ввиду Голден Фредди?", reply_markup=markup)

@bot.message_handler(content_types=["text"], func=details)
def details_(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu6 = types.KeyboardButton("Пойти")
    yu7 = types.KeyboardButton("Отказаться")
    markup.add(yu6, yu7)
    bot.send_message(message.chat.id, content["location2"]["text29"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=for_what)
def for__what(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu6 = types.KeyboardButton("Пойти")
    yu7 = types.KeyboardButton("Отказаться")
    markup.add(yu6, yu7)
    bot.send_message(message.chat.id, content["location2"]["text30"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=come_with_them)
def come__with_them(message):
    user_data_rpg[message.chat.id]['choice'] = "Пойти"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pl1 = types.KeyboardButton("играть")
    markup.add(pl1)
    bot.send_message(message.chat.id, content["location2"]["text31"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    with open("Helpi.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"Поздравляю вас, {user_data_rpg[message.chat.id]['name']}! Вы прошли второй уровень! "
                                          "Скоро вы перейдёте на следющий, только потерпите немного :)")
    time.sleep(10)
    with open("Helpi.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"Поздравляю вас, {user_data_rpg[message.chat.id]['name']}! Компания "
                                                       f"Fazbear Ent. одобрила вам переход на следующий уровень. Скорее продолжайте играть! "
                       , reply_markup=markup)

@bot.message_handler(content_types=["text"], func=delay)
def delay(message):
    user_data_rpg[message.chat.id]['choice'] = "Отказаться"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pl1 = types.KeyboardButton("играть")
    markup.add(pl1)
    bot.send_message(message.chat.id, content["location2"]["text32"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    with open("Helpi.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo,
                       caption=f"Поздравляю вас, {user_data_rpg[message.chat.id]['name']}! Вы прошли второй уровень! "
                               "Скоро вы перейдёте на следющий, только потерпите немного :)")
    time.sleep(10)
    with open("Helpi.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo,
                       caption=f"Поздравляю вас, {user_data_rpg[message.chat.id]['name']}! Компания "
                               f"Fazbear Ent. одобрила вам переход на третий уровень. Скорее продолжайте играть! "
                       , reply_markup=markup)

@bot.message_handler(content_types=["text"], func=third_variant)
def third__variant(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yu1 = types.KeyboardButton(f'Я {user_data_rpg[message.chat.id]["hero"]}')
    yu2 = types.KeyboardButton('Зачем тебе знать?')
    markup.add(yu1, yu2)
    bot.send_message(message.chat.id, content["location2"]["text33"], reply_markup=types.ReplyKeyboardRemove())
    time.sleep(20)
    with open("Pizzeria.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="Заброшенная пиццерия? 'Выглядит криповенько...'-подумали вы.")
    time.sleep(15)
    bot.send_message(message.chat.id, content["location2"]["text25"])
    with open("Animatronics2.jpg", "rb") as photo:
        time.sleep(15)
        bot.send_photo(message.chat.id, photo, caption="Четырёх сломанных аниматроников...Лиса, Медведь, Кролик и Курица..."
                                                   "Вероятно они когда-то были талисманами "
                                                   "данной пиццерии.")
    time.sleep(5)
    bot.send_message(message.chat.id, content["location2"]["text26"], reply_markup=markup)

@bot.message_handler(content_types=["text"], func=play_2)
def play__2(message):
        #enemy_atack = (random.choice(atacks_springtrap))
    bot.send_message(message.chat.id, content["location2"]["text34"], reply_markup=types.ReplyKeyboardRemove())
    with open("Springtrap.jpg", "rb") as photo:
        time.sleep(15)
        bot.send_photo(message.chat.id, photo, caption="Спрингтрапа!")
    time.sleep(3)
    bot.send_message(message.chat.id,  content["location2"]["text35"])
    if user_data_rpg[message.chat.id]['choice'] == "Пойти":
        bot.send_message(message.chat.id, content["location2"]["text37"])
    if user_data_rpg[message.chat.id]['choice'] == "Отказаться":
        bot.send_message(message.chat.id, content["location2"]["text38"])
    time.sleep(5)
    with open("Helpi.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"{user_data_rpg[message.chat.id]['name']}, вот вы и прошли главу "
                                                       f"FNAF:Overthrow! Игра находится в стадии разработки, поэтому возможно она "
                                                       f"показалась вам скучной и недолгой, но не расстраивайтесь! Скоро она пополнится "
                                                       f"новыми главами и станет куда больше!")

        #while health1 > 0:
            # = 150
            #damage -= enemy_atack
            #time.sleep(5)
            #bot.send_message(message.chat.id, f"Вам нанесли урон: {enemy_atack}")
            #bot.send_message(message.chat.id, f"Ваше здоровье: {damage}")
            #if damage == 0:
                #bot.send_message(message.chat.id, "Вы проиграли!")
                #break









@bot.message_handler(content_types=["text"])
def wrong_text(message):
    photo1_0 = open("Helpi.jpg", "rb")
    if(message.text != content["location1"]["buttons"]):
        bot.send_photo(message.chat.id, photo1_0, "Ты что-то не то вводишь! Нажимай на кнопки")
    photo1_0.close()






bot.polling()