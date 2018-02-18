import pyautogui


input("Aim your cursor then press 'Enter' to continue...")
p = pyautogui.position()
q = pyautogui.pixel(*p)
print("pixel position = ", p)
print("pixel color = ",q)

input("Save these values in constants.py. Press 'Enter' to finish up.")