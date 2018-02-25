import pyautogui
import sys


if __name__ == '__main__':  # print("  Pixel(position={}, color={})".format(p, q))
    if len(sys.argv) == 3:
        _, x, y = sys.argv
        p = (int(x), int(y))
        print("pixel position === ", p)
        print("pixel color ====== ", pyautogui.pixel(*p))
    else:
        input("Aim your cursor then press 'Enter' to continue...")
        p = pyautogui.position()
        q = pyautogui.pixel(*p)
        print("pixel position === ", p)
        print("pixel color ====== ", q)
    print("Save these values in constants.py.")
