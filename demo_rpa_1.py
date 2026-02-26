import pyautogui
import time
'''''
print ("Hello, welcome to the RPA demo. This demo will show you how to use pyautogui to automate some tasks on your computer.")
time.sleep(6) # wait for 6 seconds
pyautogui.rightClick(100, 100) # right click at the coordinates (100, 100)
time.sleep(5) # wait for 5 seconds
pyautogui.moveTo(200, 200) # move the mouse to the coordinates (200, 200)
time.sleep(5) # wait for 5 seconds

x, y = pyautogui.position() # get the current mouse position
print(f"The current mouse position is: ({x}, {y})") # print the current mouse position
time.sleep(5) # wait for 5 seconds
'''
#keyboard automation
#pyautogui.write("Hello, this is a test of pyautogui keyboard automation.") # type the text
time.sleep(5) # wait for 5 setest_file.txt

pyautogui.press('enter') # press the enter key
time.sleep(5) # wait for 5 seconds  
pyautogui.hotkey('ctrl', 's') # press the ctrl + s hotkey
time.sleep(5) # wait for 5 seconds
#pyautogui.write('test_file.txt') # type the file name
time.sleep(5) # wait for 5 seconds
pyautogui.press('enter') # press the enter key
time.sleep(5) # wait for 5 seconds
pyautogui.hotkey('ctrl', 'a') # press the ctrl + a hotkey to select all text
time.sleep(5) # wait for 5 seconds
pyautogui.hotkey('ctrl', 'c') # press the ctrl + c hotkey to copy the selected text
time.sleep(5) # wait for 5 seconds
print("The RPA demo is complete. Thank you for watching!")
pyautogui.size() # get the screen size




print(f"The screen size is: {pyautogui.size()}") # print the screen size
#pyautogui.screenshot('screenshot.png') # take a screenshot and save it as 'screenshot.png'
print("A screenshot has been taken and saved as 'screenshot.png'.") # print a message to indicate that the screenshot has been taken    
