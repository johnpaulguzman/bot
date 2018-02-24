import pyautogui
import threading
import time
#import sqlite3

from constants import Constants, Pixel

class BuffUnit:
    def __init__(self, key, pixel):
        self.key = key
        self.pixel = pixel

class Buffer(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.buffs = [
            #BuffUnit(key='f2', pixel=Pixel(position=(1324, 211), color=(203, 254, 254))),  # endure
        ]
        self.teleporter = teleporter

    def do_buffs(self):
        for buff in self.buffs:
            if not buff.pixel.is_pixel_detected():
                pyautogui.new_press(buff.key)

    def run(self):
        if not self.buffs or self.teleporter.teleporting_status: return
        while True:
            self.do_buffs()
            time.sleep(Constants.global_refresh_time)