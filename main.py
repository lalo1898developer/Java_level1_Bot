# >> Imports necesarios
import telebot
import os
from Utils.Keyboards import get_main_keyboard,get_clear_keyboard
from Services.Java import Java
from Services.JokeAPI import JokeAPI
from Services.UnplashAPI import UnplashAPI
# <<

# >> Inicializar bot
API_TOKEN = os.getenv('TOKEN_TELEBOT')
bot = telebot.TeleBot(API_TOKEN)
# <<

# >> Servicios
java = Java()
joke_api = JokeAPI()
unplash_api = UnplashAPI()
# <<

# >> Mensaje de bienvenida
with open('Docs/welcome.md','r',encoding="utf8") as f:
    welcome = f.read()

@bot.message_handler(commands=['start'])
def send_bienvenida(message):
    bot.reply_to(message, welcome, parse_mode='Markdown')
# <<

# >> Teclado
@bot.message_handler(commands=['teclado'])
def send_keyboard(message):
    markup = get_main_keyboard()
    bot.send_message(message.chat.id, "Selecciona una opción: ", reply_markup=markup)
# <<

# >> Help
@bot.message_handler(commands=['help'])
def send_help(message):
    helpfile=open("Docs/help.md", "r", encoding="utf8")
    text=helpfile.read()
    helpfile.close()
    bot.reply_to(message, text, parse_mode='Markdown')
# <<

# >> Temas de Java
@bot.message_handler(regexp="^(tema)")
def send_tema(message):
    textfile = java.get_file(message)
    bot.reply_to(message, textfile, parse_mode='Markdown')
# <<

# >> Acciones del teclado
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    # Lecciones Java
    if text == "Java":
        filenames_list = java.get_filenames()
        filenames_list.insert(0, 'Estos son los temas disponibles para aprender, escribe el que quieras para conocer mas sobre Java:')
        filenames_string = '\n'.join(filenames_list)
        bot.reply_to(message, filenames_string)

    # Jokes
    elif text == "Jokes":
        joke = joke_api.get_joke()
        if joke != None:
            bot.reply_to(message, joke)
        else:
            bot.reply_to(message,"Ocurrio un error con la API de chistes")
    
    # Imagenes
    elif text == "Image":
        image = unplash_api.get_image()
        if image != None:
            bot.reply_to(message, image, parse_mode='Markdown')
        else:
            bot.reply_to(message,"Ocurrio un error con la API de imagenes")

    # Quitar teclado
    elif text == "Quitar teclado":
        markup = get_clear_keyboard()
        bot.send_message(message.chat.id, "Escribe `/teclado` para mostrarlo.", reply_markup=markup, parse_mode='Markdown')
    else:
        bot.reply_to(message,"No entiendo tu mensaje. Escribe: /help")
# <<

bot.polling()
