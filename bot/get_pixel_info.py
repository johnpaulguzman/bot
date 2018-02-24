import pyautogui

input("Aim your cursor then press 'Enter' to continue...")
p = pyautogui.position()
q = pyautogui.pixel(*p)
print("  Pixel(position={}, color={})".format(p, q))
print("Save this value in constants.py.")