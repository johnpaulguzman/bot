import pyautogui, time


def type_enter(msg):
    pyautogui.typewrite(msg)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(1)

time.sleep(3)
items = [526, 518, 604]

#type_enter("@alootid reset")
for item in items: type_enter("@alootid +" + str(item))