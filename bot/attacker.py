import math
import pyautogui
import random
import threading
import time

import constants


class Detector:
    def __init__(self): 
        self.cursor_color_threshold = 30
        self.cursor_border_x = 1
        self.cursor_border_y = 1
        self.cursor_border_y_end = 4

    def is_clickable(self, position):
        for j in range(self.cursor_border_y, self.cursor_border_y_end + 1):
            check_pixel = pyautogui.pixel(position[0] + self.cursor_border_x, position[1] + j)
            for color in check_pixel:
                if color > self.cursor_color_threshold:
                    return True
        return False


class Attacker(threading.Thread):
    def __init__(self, teleporter):
        super().__init__(daemon=True)
        self.skill_key = constants.skill_key
        self.skill_delay = 0.005
        self.view_refresh_px = constants.view_refresh_px
        self.view_center_px = constants.view_center_px
        self.cell_size = (12, 12)  # px/cell length
        self.vision_range = 12
        self.snap_range = 3
        self.cursor_stabilize_iterations = 2
        self.partitions = math.ceil(self.vision_range / (self.snap_range * 2))
        self.ranges_to_check = [self.snap_range * 2 * p for p in range(-self.partitions + 1, self.partitions)]
        self.cells_to_check = [(x, y) for x in self.ranges_to_check for y in self.ranges_to_check]
        self.cells_to_check.sort(key = lambda p: (p[0]**2 + p[1]**2)**0.5)
        self.pixels_to_check = [(self.view_center_px[0] + cell_x * self.cell_size[0], self.view_center_px[1] + cell_y * self.cell_size[1]) for (cell_x, cell_y) in self.cells_to_check]
        self.pixels_to_check.insert(len(self.pixels_to_check) // 2, self.pixels_to_check[0])
        self.pixels_to_check.insert(len(self.pixels_to_check), self.pixels_to_check[0])
        self.random_walk_pixels = [
            (self.view_center_px[0], self.view_center_px[1] + self.vision_range * self.cell_size[1]),
            (self.view_center_px[0], self.view_center_px[1] - self.vision_range * self.cell_size[1]),
            (self.view_center_px[0] + self.vision_range * self.cell_size[0], self.view_center_px[1]),
            (self.view_center_px[0] - self.vision_range * self.cell_size[0], self.view_center_px[1]),
        ]
        self.detector = Detector()
        self.teleporter = teleporter
        pyautogui.click(self.view_center_px)

    def option_select_action(self, pixel):
        pyautogui.click(pixel)
        for _ in range(2):
            pyautogui.press(self.skill_key)
            time.sleep(self.skill_delay)
            pyautogui.click(pixel)

    def do_random_walk(self):
        random_walk_pixel = random.choice(self.random_walk_pixels)
        self.option_select_action(random_walk_pixel)
    
    def move_mouse(self):
        if self.teleporter.teleporting_status: return
        for pixel in self.pixels_to_check:
            for _ in range(self.cursor_stabilize_iterations): pyautogui.moveTo(self.view_refresh_px)
            for _ in range(self.cursor_stabilize_iterations): pyautogui.moveTo(pixel)
            if self.detector.is_clickable(pixel):
                self.option_select_action(pixel)
                return
        self.teleporter.do_teleport()
        self.do_random_walk()

    def run(self):
        while True:
            self.move_mouse()
            time.sleep(constants.global_refresh_time)