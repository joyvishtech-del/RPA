import pyautogui
import time
import subprocess

# Safety: Move mouse to top-left corner to abort
pyautogui.FAILSAFE = True

# Step 1: Open Chrome
subprocess.Popen("start chrome", shell=True)
time.sleep(3)  # Wait for browser to open

# Step 2: Focus address bar (Ctrl + L)
pyautogui.hotkey("ctrl", "l")
time.sleep(1)

# Step 3: Type search query
pyautogui.write("AI summit india", interval=0.05)
pyautogui.press("enter")

time.sleep(3)  # Wait for search results to load

# Step 4: Click first search result
# First result usually appears around this region
# (Adjust if your resolution differs)

screen_width, screen_height = pyautogui.size()
print(pyautogui.size())

# Approximate position for first search result title
#click_x = screen_width // 2
#click_y = int(screen_height * 0.35)
time.sleep(5) # wait for 5 seconds
#pyautogui.moveTo(click_x, click_y, duration=0.5)
pyautogui.click(2861, 736)  # Click on the first search result (adjust coordinates as needed)
time.sleep(5)  # Wait for page to load  


print("Automation completed successfully.")