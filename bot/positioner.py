import win32gui

class Positioner:
    def __init__(self, window_position=(0, 0)):
        self.window_name = "TalonRO 2012-10-12"
        self.window_size = (1286, 745)  # 1280, 720 in the settings
        self.window_position = window_position
        self.window_hwnd = win32gui.FindWindow(None, self.window_name)
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