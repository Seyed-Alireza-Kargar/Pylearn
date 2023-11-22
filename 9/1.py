import random
import time
import datetime
import gtts
import qrcode
from persiantools.jdatetime import JalaliDate
import telebot
from telebot import types

bot = telebot.TeleBot("6356938804:AAHAmYoSRW8RWPFOsm0NT9mTcVHkPgwOK7s", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
item_list = ["/game", "/age", "/voice", "/max", "/index_max", "/qrcode", "/help"]
for item in item_list:
    markup.add(telebot.types.KeyboardButton(item))

number = random.randint(1, 100)
chat_id = None

exit_markup = types.ReplyKeyboardMarkup(row_width=3)
exit_button = types.KeyboardButton("خروج از بازی")
exit_markup.add(exit_button)
is_in_game = {}


easy = "1 تا 10"
medium = "1 تا 50"
hard = "1 تا 100"
ch_arr = ""

@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"سلام {user_name} عزیز\nبه بات خودت خوش اومدی 😍🤍", reply_markup=markup)

# Game
@bot.message_handler(commands=["game"])
def start_game(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_markup1 = types.KeyboardButton(f"آسان ({easy})")
    item_markup2 = types.KeyboardButton(f"متوسط ({medium})")
    item_markup3 = types.KeyboardButton(f"سخت ({hard})")
    markup.add(item_markup1, item_markup2, item_markup3)
    msg = bot.send_message(message.chat.id, "سطح مورد نظرت رو برای انجام بازی انتخاب کن:", reply_markup=markup)
    bot.register_next_step_handler(msg, select_difficulty)

def select_difficulty(message):
    ch_arr = ""
    user_choice = message.text
    if user_choice == "آسان (1 تا 10)":
        number = random.randint(1, 10)
        ch_arr += easy
    elif user_choice == "متوسط (1 تا 50)":
        number = random.randint(1, 50)
        ch_arr += medium
    elif user_choice == "سخت (1 تا 100)":
        number = random.randint(1, 100)
        ch_arr += hard
        
    chat_id = message.chat.id
    is_in_game[chat_id] = True
    msg = bot.send_message(chat_id, f"سید شنیدم حدس زدنت خوبه بگو بینم عدد چنده بنظرت؟؟ \n عدد بین اعداد {ch_arr} وجود داره", reply_markup=exit_markup)
    bot.register_next_step_handler(msg, lambda m: guess_number(m, number))

def guess_number(message, number):
    chat_id = message.chat.id

    try:
        guess = int(message.text)
    except ValueError:
        if message.text == "خروج از بازی":
          is_in_game[chat_id] = False 
          markup = types.ReplyKeyboardMarkup(row_width=3)
          item_markup1 = types.KeyboardButton("/game")
          item_markup2 = types.KeyboardButton("/age")
          item_markup3 = types.KeyboardButton("/voice")
          item_markup4 = types.KeyboardButton("/max")
          item_markup5 = types.KeyboardButton("/index_max")
          item_markup6 = types.KeyboardButton("/qrcode")
          item_markup7 = types.KeyboardButton("/help")
          markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)
          bot.send_message(chat_id, "به منوی اصلی برگشتید.", reply_markup=markup)
        else :
          bot.send_message(chat_id, "لطفا یک عدد وارد کنید.")
        return

    if guess > number:
        msg = bot.send_message(chat_id, "عددی که انتخاب کردید بزرگتر از عدد درست است. پس بیا پایین تر!")
        bot.register_next_step_handler(msg, lambda m: guess_number(m, number))
    elif guess < number:
        msg = bot.send_message(chat_id, "عددی که انتخاب کردید کوچکتر از عدد درست است. پس برو بالاتر!")
        bot.register_next_step_handler(msg, lambda m: guess_number(m, number))
    elif guess == number:
        bot.send_message(chat_id, "برنده شدی!")
        is_in_game[chat_id] = False
        markup = types.ReplyKeyboardMarkup(row_width=3)
        item_markup1 = types.KeyboardButton("/game")
        item_markup2 = types.KeyboardButton("/age")
        item_markup3 = types.KeyboardButton("/voice")
        item_markup4 = types.KeyboardButton("/max")
        item_markup5 = types.KeyboardButton("/index_max")
        item_markup6 = types.KeyboardButton("/qrcode")
        item_markup7 = types.KeyboardButton("/help")
        markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)
        bot.send_message(chat_id, "به منوی اصلی برگشتید.", reply_markup=markup)

# Age calculation
@bot.message_handler(commands=["age"])
def get_birthday(message):
    msg = bot.send_message(message.chat.id, "دوس داری بهت بگم چند سالته؟؟😉 \n پس حالا تاریخ تولدتو مثل متن زیر بنویس : \n 1350/05/09")
    bot.register_next_step_handler(msg, calculate_age)

def calculate_age(message):
    birthday_year, birthday_month, birthday_day = map(int, message.text.split("/"))
    miladi_date = JalaliDate(birthday_year, birthday_month, birthday_day).to_gregorian()
    age_timedelta = datetime.date.today() - miladi_date
    age_years = age_timedelta.days // 365
    bot.send_message(message.chat.id, f"سن شما {age_years} سال است")

# Text to voice
@bot.message_handler(commands=["voice"])
def get_text(message):
    msg = bot.send_message(message.chat.id, "لطفا یک جمله به انگلیسی وارد کنید")
    bot.register_next_step_handler(msg, text_to_voice)

def text_to_voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("/home/voice.mp3")
    with open("/home/voice.mp3", "rb") as voice_file:
        bot.send_voice(message.chat.id, voice_file)

# Maximum number
@bot.message_handler(commands=["max"])
def get_numbers(message):
    msg = bot.send_message(message.chat.id, "لطفا یک آرایه از اعداد را وارد کن تا من بهت بگم بزرگترین عددش کدومه \n مثال 14,7,78,15,8,19,20)")
    bot.register_next_step_handler(msg, print_max)

def print_max(message):
    list_input = list(map(int, message.text.split(",")))
    max_number = max(list_input)
    bot.send_message(message.chat.id, f"بزرگترین عدد در لیست اعداد {list_input}: {max_number}")

# Index of maximum number
@bot.message_handler(commands=["index_max"])
def get_numbers(message):
    msg = bot.send_message(message.chat.id, "لطفا یک آرایه از اعداد را وارد کنید (مثلا: 14,7,78,15,8,19,20)")
    bot.register_next_step_handler(msg, print_index_max)

def print_index_max(message):
    numbers = list(map(int, message.text.split(",")))
    max_index = numbers.index(max(numbers))
    bot.send_message(message.chat.id, f" بزرگترین عدد این آرایه در خانه : {max_index} وجود دارد.")

# QR code
@bot.message_handler(commands=["qrcode"])
def get_text(message):
    msg = bot.send_message(message.chat.id, "لطفا متن وارد کنید")
    bot.register_next_step_handler(msg, create_QRCode)

def create_QRCode(message):
    text = message.text
    sent_message = bot.send_message(message.chat.id, "درحال ساخت لینک برای شما...\n[ ▱ ▱ ▱ ▱ ]")

    for i in range(4):
        time.sleep(1)
        progress = "".join(["▰" if j <= i else "▱" for j in range(4)])
        bot.edit_message_text(f"درحال ساخت لینک برای شما...\n[ {progress} ]", message.chat.id, sent_message.message_id)
    
    bot.delete_message(message.chat.id, sent_message.message_id)
    qr_img = qrcode.make(text)
    qr_img.save("/home/qrcode.png")
    with open("/home/qrcode.png", "rb") as qr_file:
        bot.send_photo(message.chat.id, qr_file)

# Help
@bot.message_handler(commands=["help"])
def help_user(message):
    bot.reply_to(message, "امیدوارم که از بات خوشت بیاد برای فهمیدن دستورایی که بات میتونه جوابتو بده میتونی از داکیومنت زیر استفاده کنی :")
    bot.send_message(message.chat.id,
                    "/game: بازی حدس کلمات شروع میشه"
                    "\n /age: اگر تاریخ تولدت رو بگی دقیق حساب میکنه که چند سالت هست"
                    "\n /voice: اگر بهش یه جمله انگلیسی بدی بهت یهویس از همون جملت میده"
                    "\n /max: اگر یه لیست از اعداد بدی بهت میگه کدومش بزرگ تره"
                    "\n /index_max: اگر یه لیست از اعداد بدی بهت میگه توی کدوم خونه بزرگترین عدد هست"
                    "\n /qrcode: اگر بهش یه جمله بدی برات تبدیل به QRcode میکنه"
                    "\n /help: این هم که الان زدی ولی خب این بهت لیست کامند هارو نشون میده")

bot.infinity_polling()
