r""" == REMINDERS == 
1.) Set windowed mode resolution to (1280, 720).
2.) Open the in-game options > Graphic Options:
2.a) Check Snap for attack, skill, item
2.b) /nc = off, /ns = off, /exall, /nt = on, /camera = on
3.) Center the screen (double right-click) and zoom out (mouse scroll-up) as far as possible
4.) Run the program through the command prompt (Win+r > cmd)
4.a) Run: cd bot
4.b) Run: python mainbot.py
4.c) To stop the program, Alt-Tab to cmd and input: Ctrl+C 
"""

from positioner import Positioner

from enum import Enum
import pyautogui

class Servers(Enum):
    TALONRO = 1
    NOVARO = 2

def overrider_click(*args, **kwargs):
    pyautogui.mouseDown(*args, **kwargs)
    pyautogui.mouseUp(*args, **kwargs)
    
def overrider_press(*args, **kwargs):
    pyautogui.keyDown(*args, **kwargs)
    pyautogui.keyUp(*args, **kwargs)
    
pyautogui.new_click = overrider_click
pyautogui.new_press = overrider_press


server_choice = Servers.TALONRO

class Pixel:
    black_color_threshold = 30
#
    def __init__(self, position=None, color=None):
        self.position = position
        self.color = color
#
    def translate(self, dx=0, dy=0):
        translated_position = (self.position[0] + dx, self.position[1] + dy) if self.position else None
        return Pixel(position=translated_position, color=self.color)
#
    def is_pixel_detected(self):
        if self.position == None or self.color == None:
            return False
        return pyautogui.pixel(*self.position) == self.color
#
    def is_pixel_white(self):
        for primary_color in self.color:
            if primary_color > self.black_color_threshold:
                return True
        return False

class Constants:
    RO_window_position = (0, 0)  # do as coordinate and "+" this to the coordinates
    positioner = Positioner(RO_window_position)

    if server_choice == Servers.TALONRO:
        global_refresh_time = 0.02
        cell_size = (12, 12)
        r""" new positions
        view_center_px = (634, 382)  # get pixel position of the center of the cell containing player's feet sprite
        hp_position = (150, 80)  # pixel position of 75% of the HP bar in the Ctrl+V window
        missing_hp_color = (230, 230, 238)  # (triggers heal) pixel color of hp_position when getting damaged
        critical_hp_position = (107, 80)  # pixel position of 25% of the HP bar in the Ctrl+V window
        critical_missing_hp_color = (230, 230, 238)  # (triggers teleport away) pixel color of critical_hp_position when getting damaged
        dead_hp_position = (41, 80)
        dead_hp_color = (230, 230, 238)
        open_info_position = (216, 64)
        open_info_color = (123, 156, 222)
        ks_warn_position = (634, 64)
        ks_warn_color = (181, 255, 181)
        """
        skill_key = 'f3'  # bowling bash key
        teleport_key = 'f9'  # teleport key
        heal_key = 'f1'  # consumable healing item key
        
        heal_multiples = 4   # number of consumes per heal trigger
        teleport_time = 120  # force teleport every specified seconds interval
        scroll_up_multiples = 1  # number of scroll ups inputs after each random walk
        dead_check_interval = 30
        ks_check_interval = 3
        arm_alarm = True

        view_center_pixel = Pixel(position=(716, 382))  # get pixel position of the center of the cell containing player's feet sprite
        heal_trigger_pixel = Pixel(position=(225, 80), color=(230, 230, 238))
        escape_trigger_pixel = Pixel(position=(170, 80), color=(230, 230, 238))
        death_alarm_pixel = Pixel(position=(114, 80), color=(230, 230, 238))
        info_open_pixel = Pixel(position=(288, 69), color=(123, 156, 222))
        ks_warn_pixel = Pixel(position=(708, 64), color=(181, 255, 181))


    elif server_choice == Servers.NOVARO:
        global_refresh_time = 0.02
        heal_multiples = 4  # number of consumes per heal trigger
        teleport_time = 120 # force teleport every specified seconds interval
        scroll_up_multiples = 1 # number of scroll ups inputs after each random walk
        dead_check_interval = 30
        arm_alarm = True
        ks_check_interval = 3
        cell_size = (12, 12)

        view_center_px = (718, 380)
        hp_position = (179, 80)
        missing_hp_color = (230, 230, 238)
        critical_hp_position = (146, 80)
        critical_missing_hp_color = (230, 230, 238)
        dead_hp_position = (123, 80)
        dead_hp_color = (230, 230, 238)
        open_info_position = (182, 83)
        open_info_color = (173, 197, 238)
        ks_warn_position = (708, 64)  # NONE
        ks_warn_color = (181, 255, 181)  # NONE

        skill_key = 'f3'  # bowling bash key
        teleport_key = 'f9'  # teleport key
        heal_key = 'f1'  # consumable healing item key 