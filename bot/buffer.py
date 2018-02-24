import pyautogui
import threading
import time
#import sqlite3

from constants import Constants

class BuffUnit:
    def __init__(self, key, position, color):
        self.key = key
        self.position = position
        self.color = color

class Buffer(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.buffs = [
            #BuffUnit('f2', (1324, 211), (203, 254, 254)),  # endure
        ]
        self.teleporter = teleporter

    def do_buffs(self):
        for buff in self.buffs:
            if not pyautogui.pixel(*buff.position) == buff.color:
                pyautogui.new_press(buff.key)

    def run(self):
        if not self.buffs or self.teleporter.teleporting_status: return
        while True:
            self.do_buffs()
            time.sleep(Constants.global_refresh_time)