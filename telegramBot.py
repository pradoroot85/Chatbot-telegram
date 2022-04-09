from numpy import imag
from Botyoutube import youtubeBot
from Botnetflix import netflixBot
from Botinsta import instaBot
import blockdisplaypc
import cancelshutdown
import shutdownpc
import rebootpc
import updatepc
import telebot
import msgBot
import voz1
import voz2

chave_api = ''

bot = telebot.TeleBot(chave_api)

def verificar(mensagem):
    if mensagem.text == 'Updatepc':
        updatepc.update()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu linux foi atualizado')

def verificar(mensagem):
    if mensagem.text == 'Msgface':
        msgBot.messagerBot()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, f'Enviei menssagem para \n{msgBot.nome}\n')

def verificar(mensagem):
    if mensagem.text == 'Vagas':
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    vagas = open('./vagas.txt', 'rb')
    bot.send_document(mensagem.chat.id, vagas)

def verificar(mensagem):
    if mensagem.text == 'Menu':
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    menu = ('menu\n(1)Updatepc\n(2)Msgface\n(3)Vagas\n(4)Insta\n(5)Youtube\n(6)Netflix\n(7)Desligar\n(8)Desligarc\n(9)Blocktela\n(10)Reiniciar\n(11)falalinux1\n(12)falalinux2')
    bot.send_message(mensagem.chat.id, menu)

def verificar(mensagem):
        return True

@bot.message_handler(commands=['start'])
def responder(mensagem):
    menu = ('Oi tudo bem?\nEstou pronto para te ajudar\na gerenciar o seu linux,\ne só digitar o comando (Menu)\npara ver as opções.')
    bot.send_message(mensagem.chat.id, menu)

def verificar(mensagem):
    if mensagem.text == 'Insta':
        instaBot.insta()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Instagram aberto.')

def verificar(mensagem):
    if mensagem.text == 'Netflix':
        netflixBot.abrirNetflix()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Netflix aberta')

def verificar(mensagem):
    if mensagem.text == 'Youtube':
        youtubeBot.youtube()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Youtube aberto.')

def verificar(mensagem):
    if mensagem.text == 'Blocktela':
        blockdisplaypc.blockdisplay()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Tela linux bloqueada.')

def verificar(mensagem):
    if mensagem.text == 'Desligar':
        shutdownpc.desligar()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu linux vai ser desligado.')

def verificar(mensagem):
    if mensagem.text == 'Desligarc':
        cancelshutdown.cancelpoweroff()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Seu linux cancelou o desligamento.')

def verificar(mensagem):
    if mensagem.text == 'Reiniciar':
        rebootpc.reiniciar()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Reiniciando linux')

def verificar(mensagem):
    if mensagem.text == 'Falalinux1':
        voz1.falar1()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Será??? digita Menu ai.')

def verificar(mensagem):
    if mensagem.text == 'Falalinux2':
        voz2.falar2()
        return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.send_message(mensagem.chat.id, 'Até mais...\ncanal youtube: Deploybots')


bot.polling()