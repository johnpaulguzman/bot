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

from positioner import Positioner, Servers

import pyautogui


def new_click(*args, **kwargs):
    pyautogui.mouseDown(*args, **kwargs)
    pyautogui.mouseUp(*args, **kwargs)
    
def new_press(*args, **kwargs):
    pyautogui.keyDown(*args, **kwargs)
    pyautogui.keyUp(*args, **kwargs)
    
pyautogui.new_click = new_click
pyautogui.new_press = new_press
pyautogui.mouseUp()
pyautogui.mouseUp(button='right')

class Pixel:  # TODO New branch
    def __init__(self, position, color):
        self.position = position
        self.color = color
    
    def is_detected(self):
        if self.position == None or self.color == None:
            return False
        else:
            return pyautogui.pixel(*self.position) == self.color

class Constants:
    RO_window_position = (0, 0)  # do as coordinate and "+" this to the coordinates
    positioner = Positioner(RO_window_position)
    kill_time = 120

    if positioner.server == Servers.TALONRO:
        global_refresh_time = 0.02
        do_loot = True  # include click before skill cast
        heal_interval = 0.1
        heal_multiples = 4  # number of consumes per heal trigger
        teleport_time = 120 # force teleport every specified seconds interval
        do_simple_teleport = False
        scroll_up_multiples = 1 # number of scroll ups inputs after each random walk
        dead_check_interval = 30
        arm_dead_alarm = True
        arm_map_alarm = True
        ks_check_interval = 3
        cell_size = (12, 12)
        vision_range = 12

        view_center_px = (positioner.window_size[0] // 2, positioner.window_size[1] // 2)  # get pixel position of the center of the cell containing player's feet sprite
        hp_position = (150, 80)  # pixel position of 75% of the HP bar in the Ctrl+V window
        missing_hp_color = (230, 230, 238)  # (triggers heal) pixel color of hp_position when getting damaged
        critical_hp_position = (107, 80)  # pixel position of 25% of the HP bar in the Ctrl+V window
        critical_missing_hp_color = (230, 230, 238)  # (triggers teleport away) pixel color of critical_hp_position when getting damaged
        dead_hp_position = (41, 80)
        dead_hp_color = (230, 230, 238)
        map_warn_position = (1188, 157)  # pick a dark pixel in the solid mode (Ctrl+Tab) minimap that distinguishes your preferred map
        map_warn_color = (0, 0, 0)
        open_info_position = (216, 64)
        open_info_color = (123, 156, 222)
        ks_warn_position = (634, 64)
        ks_warn_color = (181, 255, 181)
        
        skill_key = 'f3'  # bowling bash key
        teleport_key = 'f9'  # teleport key
        heal_key = 'f1'  # consumable healing item key

    elif positioner.server == Servers.NOVARO:
        global_refresh_time = 0.02
        do_loot = False
        heal_interval = 999 ###
        heal_multiples = 4  # number of consumes per heal trigger
        teleport_time = 6 # force teleport every specified seconds interval
        do_simple_teleport = True
        scroll_up_multiples = 1 # number of scroll ups inputs after each random walk
        dead_check_interval = 10
        arm_dead_alarm = True
        arm_map_alarm = True
        ks_check_interval = 999 ###
        cell_size = (20, 20)
        vision_range = 12

        view_center_px = (positioner.window_size[0] // 2, positioner.window_size[1] // 2)  # get pixel position of the center of the cell containing player's feet sprite
        hp_position = (136, 80)
        missing_hp_color = (230, 230, 238)
        critical_hp_position = (92, 81)
        critical_missing_hp_color = (247, 247, 247)
        dead_hp_position = (47, 79)
        dead_hp_color = (214, 222, 222)
        map_warn_position = (1188, 157)  ###
        map_warn_color = (0, 0, 0) ###
        open_info_position = (216, 64) ###
        open_info_color = (123, 156, 222) ###
        ks_warn_position = (634, 64) ###
        ks_warn_color = (181, 255, 181) ###
        
        skill_key = 'f3'  # bowling bash key
        teleport_key = 'f9'  # teleport key
        heal_key = 'f1'  # consumable healing item key