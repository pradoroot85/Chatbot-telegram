from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pandas as pd
import time
import os

arquivo = pd.read_excel('./amigos.xls')
nome = arquivo['Nome']
def messagerBot():
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile}")
    bot = webdriver.Chrome('./chromedriver', options=options)
    bot.get('https://facebook.com')
    time.sleep(3)
    for i, id in enumerate(arquivo['ID']):
        msg = arquivo.loc[i,'Mensagem']
        #nome = arquivo.loc[i,'Nome']

        bot.get(f'https://www.facebook.com/messages/t/{id}')
        time.sleep(4)
        env = bot.find_element_by_tag_name('br')
        time.sleep(2)
        env.send_keys(msg, Keys.ENTER)
        time.sleep(2)
    time.sleep(5)
    bot.close()

#messagerBot()