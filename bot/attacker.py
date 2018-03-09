import math
import pyautogui
import random
import threading
import time

from constants import Constants


class Detector:
    def __init__(self, teleporter): 
        self.black_color_threshold = 30
        self.cursor_border_x = 1
        self.cursor_border_y = 1
        self.cursor_border_y_end = 5
        self.door_border_x = 7
        self.door_border_y = 0
        self.door_border_y_end = 3
        self.teleporter = teleporter
    
    def close_dialog(self):  # TODO CONSTANTS
        dialog_position = (512, 190)
        dialog_color = (255, 255, 255)
        dialog_tries = 10
        if pyautogui.pixel(*dialog_position) == dialog_color:
            for i in range(dialog_tries):
                for j in range(dialog_tries):
                    pyautogui.new_press('down')
                    time.sleep(Constants.global_refresh_time)
                pyautogui.new_press('enter')
                time.sleep(Constants.global_refresh_time)
            self.teleporter.do_teleport(do_clicks=False)
    
    def is_pixel_white(self, pixel):
        for color in pixel:
            if color > self.black_color_threshold:
                return True
        return False

    def is_warp_portal(self, position):
        for j in range(self.door_border_y, self.door_border_y_end + 1):
            check_pixel = pyautogui.pixel(position[0] + self.door_border_x, position[1] + j)
            if self.is_pixel_white(check_pixel):  # dark right door hinge was not detected
                return False
        self.teleporter.do_teleport(do_clicks=False)  # run from warp portals
        return True

    def is_clickable(self, position):
        self.close_dialog()
        for j in range(self.cursor_border_y, self.cursor_border_y_end + 1):
            check_pixel = pyautogui.pixel(position[0] + self.cursor_border_x, position[1] + j)
            if self.is_pixel_white(check_pixel):  # dark left idle cursor was not detected 
                return not self.is_warp_portal(position)  # click if it is not pointing at a warp portal
        return False        

class Attacker(threading.Thread):
    def __init__(self, teleporter, callback):
        super().__init__(daemon=True)
        ego_density = 7  ###
        self.do_loot = Constants.do_loot
        self.skill_key = Constants.skill_key
        self.skill_delay = 0.005
        self.view_center_px = Constants.view_center_px
        self.cell_size = Constants.cell_size
        self.vision_range = Constants.vision_range
        self.snap_range = 3
        self.partitions = math.ceil(self.vision_range / (self.snap_range * 2))
        self.ranges_to_check = [self.snap_range * 2 * p for p in range(-self.partitions + 1, self.partitions)]
        self.cells_to_check = [(x, y) for x in self.ranges_to_check for y in self.ranges_to_check]
        self.cells_to_check.sort(key = lambda p: (p[0]**2 + p[1]**2)**0.5)
        self.pixels_to_check = [(self.view_center_px[0] + cell_x * self.cell_size[0], self.view_center_px[1] + cell_y * self.cell_size[1]) for (cell_x, cell_y) in self.cells_to_check]
        for i in range(ego_density + 1):
            self.pixels_to_check.insert(len(self.pixels_to_check) * i // ego_density, self.pixels_to_check[0])
        self.random_walk_pixels = [
            (self.view_center_px[0], self.view_center_px[1] + self.vision_range * self.cell_size[1]),
            (self.view_center_px[0], self.view_center_px[1] - self.vision_range * self.cell_size[1]),
            (self.view_center_px[0] + self.vision_range * self.cell_size[0], self.view_center_px[1]),
            (self.view_center_px[0] - self.vision_range * self.cell_size[0], self.view_center_px[1]),
        ]
        self.teleporter = teleporter
        self.detector = Detector(teleporter)
        self.callback = callback
        pyautogui.new_click(self.view_center_px)
        self.check_dead_position = (614, 389) # center hp bar
        self.check_dead_color = (66, 66, 66)

    def option_select_action(self, pixel):
        if self.do_loot:
            pyautogui.new_click(pixel)
            time.sleep(Constants.global_refresh_time)
        for _ in range(2):
            pyautogui.new_press(self.skill_key)
            time.sleep(self.skill_delay)
            pyautogui.new_click(pixel)

    def do_random_walk(self):
        random_walk_pixel = random.choice(self.random_walk_pixels)
        pyautogui.new_click(random_walk_pixel)
        r"""self.option_select_action(random_walk_pixel)
        for _ in range(Constants.scroll_up_multiples): 
            pyautogui.scroll(1)
            time.sleep(Constants.global_refresh_time)"""
    
    def move_mouse(self):
        # if self.teleporter.teleporting_status: return
        for pixel in self.pixels_to_check:
            if self.teleporter.teleporting_status: return
            pyautogui.new_click(button='right')
            pyautogui.moveTo(pixel)
            if self.detector.is_clickable(pixel):
                self.option_select_action(pixel)
                #return
        else:
            self.do_random_walk()
            if pyautogui.pixel(*self.check_dead_position) == self.check_dead_color: 
                self.callback(1)
        if not Constants.do_simple_teleport:  ####### wtf novaro
            self.teleporter.do_teleport()
            self.do_random_walk()

    def run(self):
        while True:
            self.move_mouse()
            time.sleep(Constants.global_refresh_time)