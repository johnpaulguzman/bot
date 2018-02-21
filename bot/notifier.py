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
        self.arm_alarm = constants.arm_alarm
        self.open_info_position = constants.open_info_position
        self.open_info_color = constants.open_info_color
        self.check_open_info()

    def check_open_info(self):
        if pyautogui.pixel(*self.open_info_position) == self.open_info_color:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('v')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('v')
        
    def sound_alarm(self):
        while True:
            print('\a')  # beep()
            time.sleep(0.5)

    def check_dead(self):
        if pyautogui.pixel(*self.dead_hp_position) == self.dead_hp_color:
            self.sound_alarm()

    def run(self):
        if not self.arm_alarm: return
        while True:
            self.check_dead()
            time.sleep(self.dead_check_interval)
