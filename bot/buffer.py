import pyautogui
import threading
import time

import constants


class Buffer(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.speed_pots_key = constants.speed_pots_key
        self.speed_pots_delay = 30 * 60
    
    def do_speed_pots(self):
        time.sleep(self.speed_pots_delay)
        pyautogui.press(self.speed_pots_key)

    def run(self):
        while True:
            self.do_speed_pots()