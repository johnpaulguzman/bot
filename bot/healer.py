import pyautogui
import threading
import time

import constants


class Healer(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.heal_key = constants.heal_key
        self.hp_position = constants.hp_position
        self.missing_hp_color = constants.missing_hp_color
        self.heal_multiples = constants.heal_multiples
        self.heal_delay = 0.1
        self.critical_hp_position = constants.critical_hp_position
        self.critical_missing_hp_color = constants.critical_missing_hp_color
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
            time.sleep(constants.global_refresh_time)
