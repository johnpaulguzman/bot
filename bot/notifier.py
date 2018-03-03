import pyautogui
import threading
import time

from constants import Constants


class Notifier(threading.Thread):
    def __init__(self, callback):
        super().__init__(daemon=True)
        self.dead_hp_position = Constants.dead_hp_position
        self.dead_hp_color = Constants.dead_hp_color
        self.dead_check_interval = Constants.dead_check_interval
        self.arm_dead_alarm = Constants.arm_dead_alarm
        self.arm_map_alarm = Constants.arm_map_alarm
        self.open_info_position = Constants.open_info_position
        self.open_info_color = Constants.open_info_color
        self.map_warn_position = Constants.map_warn_position
        self.map_warn_color = Constants.map_warn_color
        self.callback = callback
        self.check_open_info()

    def check_open_info(self):
        if pyautogui.pixel(*self.open_info_position) == self.open_info_color:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('alt')
        
    def sound_alarm(self):
        while True:
            print('\a')  # beep()
            time.sleep(0.5)

    def check_dead(self):
        if not self.arm_dead_alarm: return
        if pyautogui.pixel(*self.dead_hp_position) == self.dead_hp_color:
            self.sound_alarm()
            
    def check_map(self):
        if not self.arm_map_alarm: return
        if not pyautogui.pixel(*self.map_warn_position) == self.map_warn_color:
            self.sound_alarm()

    def run(self):
        while True:
            #self.check_dead()
            #self.check_map()
            if pyautogui.pixel(514, 480) == (115, 148, 214): self.callback(1)  ###### WTF NOVARO
            time.sleep(self.dead_check_interval)
