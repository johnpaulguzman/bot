window_size = (1280, 720)
view_refresh_px = (83, 29)  # get pixel position of a Basic Information button
view_center_px = (716, 382)  # get pixel position of the center of the cell containing player's feet sprite

skill_key = 'f3'  # bowling bash key
teleport_key = 'f9'  # teleport key
heal_key = 'f1'  # consumable healing item key

heal_multiples = 3  # number of consumes per heal trigger
hp_position = (235, 79)  # pixel position of 75% of the HP bar in the Ctrl+V window
missing_hp_color = (214, 222, 222)  # (triggers heal) pixel color of hp_position when getting damaged
critical_hp_position = (138, 80)  # pixel position of 25% of the HP bar in the Ctrl+V window
critical_missing_hp_color = (230, 230, 238)  # (triggers teleport away) pixel color of critical_hp_position when getting damaged