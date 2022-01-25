import arcade
from game.tiles import Tiles

class CheckMatch():
    """ You have to start and finish drawing in arcade using start_render() and finish_render().
    open_window()
    draw_rectangle() expects the x and y coordinates of the center of the rectangle, the width, and the height.
    
    Keyboard Input: .on_key_press(), .on_key_release()
    Mouse Input: .on_mouse_press(), .on_mouse_release(), .on_mouse_motion()
    Updating Game Object: .on_update()
    Drawing: .on_draw()"""

    def __init__(self):
        pass

# Columns:
# 1 65
# 1 165
# 1 195
# 2 295
# 2 325
# 3 425
# 3 455
# 4 555
# 4 587
# 5 686

    def get_column(self, x):
        if x >= 65 and x < 165:
            column = 1
        elif x >= 195 and x < 295:
            column = 2
        elif x >= 325 and x < 425:
            column = 3
        elif x >= 455 and x < 555:
            column = 4
        elif x >= 585 and x < 685:
            column = 5
        else:
            column = 0
        return column

# Rows:
# 1 54
# 1 154
# 1 182
# 2 282
# 2 314
# 3 413
# 3 442
# 4 541

    def get_row(self, y):
        if y >= 55 and y < 155:
            row = 1
        elif y >= 185 and y < 285:
            row = 2
        elif y >= 315 and y < 415:
            row = 3
        elif y >= 445 and y < 545:
            row = 4
        else:
            row = 0
        return row

    def get_tile(self, x, y,):
        clicked_sprite_list = arcade.get_sprites_at_point((x, y), Tiles().sprite_list)
        for i in clicked_sprite_list:
            i._set_scale(0.2)

    def check_match(self, sprite1: arcade.Sprite, sprite2: arcade.Sprite):
        name1 = sprite1.get_name()
        name2 = sprite2.get_name()
        if name1 == name2:
            return True
        else:
            return False
