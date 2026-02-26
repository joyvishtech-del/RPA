import pyautogui
import time

time.sleep(5) # wait for 5 seconds
x, y = pyautogui.position() # get the current mouse position
print(f"The current mouse position is: ({x}, {y})") # print the current mouse position
