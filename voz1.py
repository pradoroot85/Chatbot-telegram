from gtts import gTTS
import os
 
def falar1():
    frase = gTTS(text='Será que da para controlar seu linux em rede externa, com um bot do telegram, usando python?, acho que dá!, vamos ver?', lang='pt')  #pt eh o codigo de idioma correspondente ao Portugues. 
                                                                   #Aqui pode ser utilizado qualquer um dos codigos de idioma citados anteriormente neste post.
    frase.save("./audio.mp3")
    os.system("mpg321 ./audio.mp3")

#falar1()