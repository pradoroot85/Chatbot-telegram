from gtts import gTTS
import os
 
def falar2():
    frase = gTTS(text='E ai gostou?, acesse meu canal no youtube, Deploybots, até mais.', lang='pt')  #pt eh o codigo de idioma correspondente ao Portugues. 
                                                                   #Aqui pode ser utilizado qualquer um dos codigos de idioma citados anteriormente neste post.
    frase.save("./audio1.mp3")
    os.system("mpg321 ./audio1.mp3")

#falar2()