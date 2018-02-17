import pyautogui
import time

class Healer:
    def __init__(self):
        self.heal_key = 'f1'
        self.hp_position = (235, 79)
        self.missing_hp_color = (214, 222, 222)
        self.heal_multiples = 4
        self.heal_delay = 0.5
    
    def do_heal(self):
        for i in range(self.heal_multiples):
            pyautogui.press(self.heal_key)
            time.sleep(self.heal_delay)

    def run(self):
        while True:
            if pyautogui.pixel(*self.hp_position) == self.missing_hp_color:
                self.do_heal()
