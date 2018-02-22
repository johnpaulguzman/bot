import pyautogui
import threading
import time
import sqlite3

from constants import Constants

class BuffUnit:
    def __init__(self, name, interval, key):
        pass  # TODO sqlite time logging

class Buffer(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.speed_pots_key = Constants.speed_pots_key
        self.speed_pots_delay = 30 * 60
    
    def do_speed_pots(self):
        time.sleep(self.speed_pots_delay)
        pyautogui.press(self.speed_pots_key)

    def run(self):
        while True:
            self.do_speed_pots()
            time.sleep(Constants.global_refresh_time)