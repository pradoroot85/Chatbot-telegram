from selenium import webdriver
import time 
import os

def insta():
    
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={profile}")
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('https:/instagram.com/')
    driver.maximize_window()
    time.sleep(10)


#insta()
    