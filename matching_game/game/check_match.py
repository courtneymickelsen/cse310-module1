from pydoc import cli
import arcade
from game.tiles import Tiles
from game.tile import Tile

class CheckMatch():
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

    def show_image(self, x, y, sprite_list: arcade.SpriteList):
        # for tile in Tiles().sprite_list:
            # if tile.collides_with_point([x, y]):
        
        clicked_sprite_list = (arcade.get_sprites_at_point(point= [x, y], sprite_list = sprite_list))
        print(clicked_sprite_list)
        for i in clicked_sprite_list:
            # i.filename= i.path
            i.flip( sprite_list)

    def check_match(self, sprites: arcade.SpriteList):
        name1 = sprites[0].image
        name2 = sprites[1].image
        # debugging
        print(f'Comparing {name1} and {name2}:')
        
        if name1 == name2:
            # debugging
            print('You found a match!')
            return True
        else:
            # debugging
            print('Keep looking!')
            return False
