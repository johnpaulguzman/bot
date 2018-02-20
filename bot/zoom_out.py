import pyautogui
import sys

zoom = 1
if len(sys.argv) == 2:
    zoom = -1 
while True: pyautogui.scroll(zoom)