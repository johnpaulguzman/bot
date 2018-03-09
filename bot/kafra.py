import pyautogui
import time
import subprocess

from constants import Constants


class Kafra:
    def __init__(self):
        self.buffcds = [('f7', 1) , ('f8', 4)]
        self.stay_key = 'f4'
        self.healer_postion = (576, 327)
        self.kafra_position = (693, 292)
        self.warper_position = (794, 324)
        self.inventory_tab_positions = [(761, 48), (764, 76), (765, 99)]
        self.inventory_empty_position = (798, 42)
        self.inventory_empty_color = (119, 119, 119)
        self.server_buffer = 1
        self.ammo_open_position = (1142, 470)
        self.arrow_position = (1166, 631)
        self.arrow_unequip = 'f6'
        self.arrow_equip = 'f5'
        self.arrow_amount = 5000  # this better trigger overweight
        self.kafra_close_position = (1239, 498)
        self.loading_buffer = 4
        self.return_key = '3'
        self.open_inventory_position = (891, 147)
        self.open_inventory_color = (255, 255, 255)
        self.open_ammo_position = (1228, 729)
        self.open_ammo_color = (247, 247, 247)
        self.overweight_position = (57, 145)
        self.overweight_color = (255, 0, 0)  # red font
        self.reposition_exes = ['run.exe']
    
    def open_inventory(self):
        if pyautogui.pixel(*self.open_inventory_position) != self.open_inventory_color:
            pyautogui.new_hotkey('alt', 'e')
    
    def click_npc(self, position):
        pyautogui.new_press(self.stay_key)
        pyautogui.new_click(position)
        time.sleep(self.server_buffer)
        
    def press_npc(self, key):
        pyautogui.new_press(key)
        time.sleep(self.server_buffer)
        
    def do_return(self):
        pyautogui.new_hotkey('alt', self.return_key)
        time.sleep(self.loading_buffer)    
    
    def do_recenter(self):
        subprocess.check_call(self.reposition_exes)
        time.sleep(self.server_buffer)
        # novaro client does not respond to the thiss
        r"""pyautogui.mouseDown(self.open_inventory_position)        
        time.sleep(1.0/1000 * 73)
        pyautogui.mouseUp(self.open_inventory_position)     
        time.sleep(1.0/1000 * 126)
        for i in range(10):
            pyautogui.mouseDown(self.open_inventory_position, button='right')          
            time.sleep(20/1000)
            pyautogui.mouseUp(self.open_inventory_position, button='right')
            pyautogui.mouseUp(self.open_inventory_position, button='right')    
            time.sleep(100/1000)
            pyautogui.mouseDown(self.open_inventory_position, button='right')         
            time.sleep(20/1000)
            pyautogui.mouseUp(self.open_inventory_position, button='right') 
            pyautogui.mouseUp(self.open_inventory_position, button='right') 
            time.sleep(1)"""
    
    def do_buffs(self):
        for (buff, cd) in self.buffcds:
            pyautogui.new_press(buff)
            time.sleep(cd)

    def kafra_talk(self):
        if pyautogui.pixel(*self.overweight_position) != self.overweight_color:
            return  
        self.click_npc(self.kafra_position)
        self.press_npc('enter')
        self.press_npc('down')
        self.press_npc('enter')
        self.press_npc('enter')
        pyautogui.new_press(self.arrow_unequip)
        time.sleep(self.server_buffer)
        if pyautogui.pixel(*self.open_ammo_position) != self.open_ammo_color:
            pyautogui.new_click(self.ammo_open_position)
        pyautogui.keyDown('alt')
        for tab in self.inventory_tab_positions:
            pyautogui.new_click(tab)
            pyautogui.moveTo(self.inventory_empty_position)
            time.sleep(self.server_buffer)
            while pyautogui.pixel(*self.inventory_empty_position) == self.inventory_empty_color:
                pyautogui.new_click(self.inventory_empty_position, button='right')
                time.sleep(self.server_buffer)
        pyautogui.keyUp('alt')
        pyautogui.mouseDown(self.arrow_position)
        pyautogui.mouseUp(self.inventory_empty_position)
        time.sleep(self.server_buffer)
        pyautogui.typewrite(str(self.arrow_amount))
        pyautogui.new_press('enter')
        time.sleep(self.server_buffer)
        pyautogui.new_press(self.arrow_equip)
        time.sleep(self.server_buffer)
        pyautogui.new_click(self.kafra_close_position)
        time.sleep(self.server_buffer)
    
    def warper_talk(self):
        self.click_npc(self.warper_position)
        self.press_npc('enter')
        time.sleep(self.loading_buffer)
        
    def healer_talk(self):
        self.click_npc(self.healer_postion)
        time.sleep(self.server_buffer)
    
    def run(self):
        self.open_inventory()
        self.do_return()
        self.do_recenter()
        self.healer_talk()
        self.do_buffs()
        self.kafra_talk()
        self.warper_talk()


if __name__ == '__main__':
    time.sleep(1)
    r = Kafra()
    r.run()