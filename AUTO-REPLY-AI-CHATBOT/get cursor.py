import pyautogui
import time

# Continuously print the current mouse cursor position every 0.5 seconds
try:
    while True:
        position = pyautogui.position()
        print(position)
        time.sleep(0.5)  # Add a short delay to avoid flooding the output
except KeyboardInterrupt:
    print("Stopped cursor position tracking.")

# This code is used to identify the secure