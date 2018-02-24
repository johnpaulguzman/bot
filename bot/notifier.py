import pyautogui
import threading
import time

from constants import Constants


class Notifier(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.dead_hp_position = Constants.dead_hp_position
        self.dead_hp_color = Constants.dead_hp_color
        self.dead_check_interval = Constants.dead_check_interval
        self.arm_alarm = Constants.arm_alarm
        self.open_info_position = Constants.open_info_position
        self.open_info_color = Constants.open_info_color
        self.check_open_info()

    def check_open_info(self):
        if pyautogui.pixel(*self.open_info_position) == self.open_info_color:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('alt')
        
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
