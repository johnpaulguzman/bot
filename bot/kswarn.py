import pyautogui
import threading
import time

from constants import Constants


class KSWarn(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.ks_warn_position = Constants.ks_warn_position
        self.ks_warn_color = Constants.ks_warn_color
        self.ks_check_interval = Constants.ks_check_interval
        self.teleporter = teleporter

    def check_ks(self):
        if pyautogui.pixel(*self.ks_warn_position) == self.ks_warn_color:
            self.teleporter.do_teleport(do_clicks=False)
            for _ in range(2):
                pyautogui.typewrite("/gc noted")
                pyautogui.new_press('enter')

    def run(self):
        while True:
            self.check_ks()
            time.sleep(self.ks_check_interval)
            time.sleep(Constants.global_refresh_time)
