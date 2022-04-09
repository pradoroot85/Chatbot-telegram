
import pyautogui as gui
import time 

def update():
    gui.hotkey('ctrl', 'alt', 't')
    time.sleep(2)
    gui.write('sudo apt update && apt upgrade -y')
    gui.press('Enter')
    time.sleep(1)
    gui.write('root')
    time.sleep(1)
    gui.press('Enter')

#update()