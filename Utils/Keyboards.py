from telebot import types

def get_main_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Java'))
    markup.add(types.KeyboardButton('Jokes'))
    markup.add(types.KeyboardButton('Image'))
    markup.add(types.KeyboardButton('Quitar teclado'))
    return markup

def get_clear_keyboard():
    return types.ReplyKeyboardRemove(selective=False)