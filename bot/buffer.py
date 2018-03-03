import pyautogui
import threading
import time
#import sqlite3

from constants import Constants


class BuffUnit:
    def __init__(self, key, position, color, cooldown):
        self.key = key
        #self.position = position
        self.color = color
        self.cooldown = cooldown

class Buffer(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        buff_box_size = 32
        buff_border_size = 3
        self.buff_start_position = (1235, 207)
        self.buff_rect_period = buff_box_size + buff_border_size
        self.max_buffs_number = 2
        self.buffs = [
            #BuffUnit('f2', None, (203, 254, 254), 1),  # endure
        ]
        self.teleporter = teleporter

    def do_buffs(self):
        if self.teleporter.teleporting_status: return
        for buff in self.buffs:
            if all([pyautogui.pixel(self.buff_start_position[0], self.buff_start_position[1] + i * self.buff_rect_period) != buff.color for i in range(self.max_buffs_number)]):
                #time.sleep(1/2)  ## are you really gone?
                #if all([pyautogui.pixel(self.buff_start_position[0], self.buff_start_position[1] + i * self.buff_rect_period) != buff.color for i in range(self.max_buffs_number)]):
                pyautogui.new_press(buff.key)
                time.sleep(buff.cooldown)
                return

    def run(self):
        if not self.buffs: return
        while True:
            self.do_buffs()
            time.sleep(1)  ##########
            time.sleep(Constants.global_refresh_time)