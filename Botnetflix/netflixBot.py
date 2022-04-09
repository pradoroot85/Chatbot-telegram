from selenium import webdriver 
import time 
import os


def abrirNetflix():
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile}")
    #options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('https://www.netflix.com/br/login')
    titulo = driver.title
    print('')
    print(f'O titulo da pagina é {titulo}')
    print('')
    
    
    time.sleep(10)
    
    
abrirNetflix()