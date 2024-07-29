import pyautogui
import time
import json
import random

with open('random_texts.json', 'r') as file:
    data = json.load(file)
    random_texts = data['texts']


def automate_search(text):
    pyautogui.moveTo(890, 53, duration=0.5) # Enter Your co-ordinate (You can find it by using Coordinate.py)
    pyautogui.click()
    pyautogui.typewrite(text, interval=0.1)
    pyautogui.press('enter')

    time.sleep(5) #Adjust the sleep time according your internet connection

texts_to_search = random.sample(random_texts, 30)

for text in texts_to_search:
    automate_search(text)
    time.sleep(2)
