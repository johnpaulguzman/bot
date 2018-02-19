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
        self.clicks_before_enter = 3
        self.clicks_before_enter_delay = 0.25
        self.enter_times = 2
        self.teleporting_status = False
        self.teleporting_status_time = 1
    
    def do_teleport(self, do_clicks=True):
        pyautogui.press(self.teleport_key)
        for _ in range(self.clicks_before_enter):
            if do_clicks:
                pyautogui.click()
            time.sleep(self.clicks_before_enter_delay)
        for _ in range(self.enter_times):
            pyautogui.press(self.enter_key)
        self.teleporting_status = True
        time.sleep(self.teleporting_status_time)
        self.teleporting_status = False

    def run(self):
        while True:
            self.do_teleport()
            time.sleep(self.teleport_time)
            time.sleep(constants.global_refresh_time)
