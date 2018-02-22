import pyautogui
import threading
import time

from constants import Constants


class Healer(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.heal_key = Constants.heal_key
        self.hp_position = Constants.hp_position
        self.missing_hp_color = Constants.missing_hp_color
        self.heal_multiples = Constants.heal_multiples
        self.heal_delay = 0.1
        self.critical_hp_position = Constants.critical_hp_position
        self.critical_missing_hp_color = Constants.critical_missing_hp_color
        self.teleporter = teleporter
    
    def do_heal(self):
        for i in range(self.heal_multiples):
            pyautogui.press(self.heal_key)
            time.sleep(self.heal_delay)

    def run(self):
        while True:
            if pyautogui.pixel(*self.critical_hp_position) == self.critical_missing_hp_color:
                #print("Attempting to run...")
                self.teleporter.do_teleport()
            if pyautogui.pixel(*self.hp_position) == self.missing_hp_color:
                self.do_heal()
            time.sleep(Constants.global_refresh_time)
