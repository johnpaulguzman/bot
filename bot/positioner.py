import win32gui

from enum import Enum


ERROR_NAME = "No window name match found."

class Servers(Enum):
    TALONRO = "TalonRO 2012-10-12"
    NOVARO = "Nova Ragnarok"

class Positioner:
    def __init__(self, window_position=(0, 0)):
        for s in Servers:
            self.window_hwnd = win32gui.FindWindow(None, s.value)
            if self.window_hwnd != 0:
                self.server = s
                break
        else:
            raise Exception(ERROR_NAME)
        self.window_size = (1286, 745)  # 1280, 720 in the settings
        self.window_position = window_position
        self.validate_window()
        win32gui.SetForegroundWindow(self.window_hwnd)
        win32gui.MoveWindow(self.window_hwnd, *self.window_position, *self.window_size, 1)
    
    def validate_window(self):
        try:
            window_left, window_top, window_right, window_bottom = win32gui.GetWindowRect(self.window_hwnd)
            window_width, window_height = window_right - window_left, window_bottom - window_top
            assert self.window_size == (window_width, window_height)
        except Exception as e:
            print(e)
            exit(1)