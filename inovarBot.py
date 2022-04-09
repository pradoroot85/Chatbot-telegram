
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

def vagasBot():
    options = Options()
    options.headless = True
    bot = webdriver.Chrome('./chromedriver', options=options)
    bot.get('https://inovar.tweezer.jobs/candidato/vaga/buscar_vaga/')
    time.sleep(5)
    bot.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
    bt = bot.find_element_by_tag_name('body')
    for c in range(0,3):
        time.sleep(2)
        bt.find_element_by_class_name('fa-bars').click()
        time.sleep(3)          
        vagas = bt.find_element_by_id('vagas_selecionadas').text
        resultado = open('./vagas.txt', 'w')
        resultado.write(vagas)
        resultado.close()
    bot.close()


#vagasBot()


    

