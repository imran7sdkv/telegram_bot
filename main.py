from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from key_buttons import tele_button, button, exit_exit
from menu import main_menu_keyboard, course_menu_keyboard


def record(update: Update, context: CallbackContext):
    text = update.message.text
    if text[:6] == 'Запись':
        print(text)
        context.bot.send_message(
            chat_id='-855309837',
            text=text
        )


def on_click(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""
1. Напишите сообщение "Запись: " и ваше ФИО.
2. Ваш номер телефона.
3. Выберите удобное вам время.
        """
    )

def start(update: Update, context: CallbackContext):
    
    context.bot.sendSticker(
        update.effective_chat.id,
        sticker ='CAACAgIAAxkBAAEGbWVjc3mX9VFPqHxc3HfaT5SBuF0_MwACDAADOTXQHmQDRlD5SWaEKwQ'
    )
    update.message.reply_text(
        f"Добро Пожаловать {update.effective_user.username}",
        reply_markup=main_menu_keyboard()
    )

ABOUT = tele_button[0]
COURSE_MENU = tele_button[1]
BACK = exit_exit[0]
PYTHON = button[0]
JS = button[1]
UXUI = button[2]
LOC = tele_button[2]
RECORD = button[3]

def resive_course_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup=course_menu_keyboard()
    )

def about(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Образовательное учреждение в котором люди любого возраста за короткие сроки могут получить качественное образование в сфере IT. Основная концепция OGOGO академии это дарить знания вместе с эмоциями, развивая не только технические навыки, но и личные качества наших студентов. Целью компании является взращивание новых конкурентоспособных IT специалистов для мирового рынка компьютерных технологий.',
        reply_markup=main_menu_keyboard()
    )

def back(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выполнено',
        reply_markup=main_menu_keyboard()
    )

def location(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
            update.effective_chat.id,
            text = 'Location of OGOGO'
        )
    update.message.reply_location(
        #42.873605195923126, 74.6199937538582
        longitude=74.6199937538582,
        latitude=42.873605195923126,
        reply_to_message_id=msg.message_id
    )

def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='python_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='python_lesson'),],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def js_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='js_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='js_lesson'),],
    [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )    

def uxui_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='ux/ui_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='ux/ui_lesson'),],
    [InlineKeyboardButton('Price', callback_data='ux/ui_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите опцию',
        reply_markup=reply_murkup
    )

def button(update: Update, context: CallbackContext):
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='python_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='python_lesson'),],
    [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ilias.jpeg.jpg', 'rb'),
            caption = """
name: Ilias
age: 16
expierence: 6 years
work place: Google, Microsoft, Facebook, Oazis
            """,
            reply_markup=reply_murkup
        )

    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'оплата: 16,000 сом в месяц.' 
        )
        
    if query.data == 'python_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'Уроки проходят 5 раз в неделю, длится каждый урок порядка трёх часов, также мы имеем перерыв.' 
        )

    query = update.callback_query
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='js_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='js_lesson'),],
    [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query

    if query.data == 'js_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/js.webp', 'rb'),
            caption = """
name: Ishak
age: 28
expierence: 4 years
work place: Google, Microsoft, Facebook
            """,
            reply_markup=reply_murkup
        )
    if query.data == 'js_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'оплата: 16,000 сом в месяц.' 
        )
        
    if query.data == 'js_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'Уроки проходят 5 раз в неделю, длится каждый урок порядка трёх часов, также мы имеем перерыв.' 
        )


    query = update.callback_query
    keyboard = [
    
    [InlineKeyboardButton('Mentor', callback_data='ux/ui_mentor'),],
    [InlineKeyboardButton('Lesson', callback_data='ux/ui_lesson'),],
    [InlineKeyboardButton('Price', callback_data='ux/ui_price')]
    ]
    reply_murkup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    
    if query.data == 'ux/ui_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ux_ui.jpg', 'rb'),
            caption = """
name: Ildar
age: 23
expierence: 5 years
work place: Google, Apple
            """,
            reply_markup=reply_murkup
        )
    if query.data == 'ux/ui_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = 'оплата: 16,000 сом в месяц.' 
        )
        
    if query.data == 'ux/ui_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = '😊Уроки проходят 5 раз в неделю, длится каждый урок порядка трёх часов, также мы имеем перерыв.' 
        )


updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_MENU),
    resive_course_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UXUI),
    uxui_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOC),
    location
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(RECORD),
    on_click
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    record
))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()