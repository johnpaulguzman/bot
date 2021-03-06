import pyautogui
import threading
import time

from constants import Constants


class Teleporter(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.teleport_key = Constants.teleport_key
        self.enter_key = 'enter'
        self.teleport_time = Constants.teleport_time
        self.clicks_before_enter = 3
        self.clicks_before_enter_delay = 0.25
        self.enter_times = 3
        self.teleporting_status = False
        self.teleporting_status_time = 1
    
    def do_teleport(self, do_clicks=True):
        pyautogui.new_press(self.teleport_key)
        for _ in range(self.clicks_before_enter):
            if do_clicks:
                pyautogui.new_click()
            time.sleep(self.clicks_before_enter_delay)
        for _ in range(self.enter_times):
            pyautogui.new_press(self.enter_key)
        self.teleporting_status = True
        time.sleep(self.teleporting_status_time)
        self.teleporting_status = False

    def run(self):
        while True:
            self.do_teleport()
            time.sleep(self.teleport_time)
            time.sleep(Constants.global_refresh_time)
