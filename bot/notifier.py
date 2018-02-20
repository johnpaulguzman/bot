import pyautogui
import threading
import time

import constants


class Notifier(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.dead_hp_position = constants.dead_hp_position
        self.dead_hp_color = constants.dead_hp_color
        self.dead_check_interval = constants.dead_check_interval

    def sound_alarm(self):
        while True:
            print('\a')  # beep()
            time.sleep(0.5)

    def check_dead(self):
        if pyautogui.pixel(*self.dead_hp_position) == self.dead_hp_color:
            self.sound_alarm()

    def run(self):
        while True:
            self.check_dead()
            time.sleep(self.dead_check_interval)
