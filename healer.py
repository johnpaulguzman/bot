import pyautogui
import time

import constants


class Healer:
    def __init__(self, teleporter):
        self.heal_key = constants.heal_key
        self.hp_position = constants.hp_position
        self.missing_hp_color = constants.missing_hp_color
        self.heal_multiples = constants.heal_multiples
        self.heal_delay = 0.5
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
                self.teleporter.do_teleport()
            if pyautogui.pixel(*self.hp_position) == self.missing_hp_color:
                self.do_heal()