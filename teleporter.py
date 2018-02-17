import pyautogui
import time

import constants


class Teleporter:
    def __init__(self):
        self.teleport_key = constants.teleport_key
        self.enter_key = 'enter'
        self.teleport_time = 180  # force teleport every specified seconds interval
        self.teleport_enter_delay = 1
        self.teleporting_status = False
        self.teleporting_status_time = 1
    
    def do_teleport(self):
        pyautogui.press(self.teleport_key)
        time.sleep(self.teleport_enter_delay)
        pyautogui.press(self.enter_key)
        self.teleporting_status = True
        time.sleep(self.teleporting_status_time)
        self.teleporting_status = False

    def run(self):
        while True:
            time.sleep(1)
            self.do_teleport()
            time.sleep(self.teleport_time)
