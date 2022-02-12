import arcade
import os
import constants
from game.tiles import Tiles
from game.check_match import CheckMatch

class StartGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.start_render()
        arcade.set_background_color([arcade.color.WHITE])
        self.t = Tiles()
        self.t.create_tiles()

    def on_mouse_press(self, x, y, button, modifiers):        
        CheckMatch().show_image(x, y, self.t.sprite_list)

        flipped = arcade.SpriteList(use_spatial_hash= True)
        
        for tile in self.t.sprite_list:
            if tile.get_name() != 'green':
                flipped.append(tile)
        if len(flipped) >= 2:
            if not (CheckMatch().check_match(flipped)):
                flipped[0].flip(self.t.sprite_list)
                flipped[1].flip(self.t.sprite_list)      