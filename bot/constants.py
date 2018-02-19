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

global_refresh_time = 0.01
view_refresh_px = (83, 29)  # get pixel position of a Basic Information button
view_center_px = (716, 382)  # get pixel position of the center of the cell containing player's feet sprite

skill_key = 'f3'  # bowling bash key
teleport_key = 'f9'  # teleport key
heal_key = 'f1'  # consumable healing item key
heal_multiples = 4  # number of consumes per heal trigger
teleport_time = 120 # force teleport every specified seconds interval
scroll_up_multiples = 1 # number of scroll ups inputs after each random walk

hp_position = (225, 80)  # pixel position of 75% of the HP bar in the Ctrl+V window
missing_hp_color = (230, 230, 238)  # (triggers heal) pixel color of hp_position when getting damaged
critical_hp_position = (170, 80)  # pixel position of 25% of the HP bar in the Ctrl+V window
critical_missing_hp_color = (230, 230, 238)  # (triggers teleport away) pixel color of critical_hp_position when getting damaged

speed_pots_key = 'f8'