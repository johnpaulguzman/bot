import pyautogui
import threading
import time

import constants


class Teleporter(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.teleport_key = constants.teleport_key
        self.enter_key = 'enter'
        self.teleport_time = constants.teleport_time
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
            self.do_teleport()
            time.sleep(self.teleport_time)
            time.sleep(constants.global_refresh_time)
