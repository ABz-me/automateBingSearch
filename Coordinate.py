import pyautogui
import time

print("Go go go... move your mouse to the desired position...")
time.sleep(5) #Adjust as per your need

x, y = pyautogui.position()
print(f"The current mouse position is: ({x}, {y})")
