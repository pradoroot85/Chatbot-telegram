from selenium import webdriver 
import time
import os


def youtube():
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile}")
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('https://www.youtube.com')
    driver.maximize_window()
    time.sleep(10)
    
    

#youtube()