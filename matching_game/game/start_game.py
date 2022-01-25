import arcade
from game import constants
from game.tiles import Tiles
from game.check_match import CheckMatch

class StartGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.set_background_color([arcade.color.WHITE])
        # self.draw_squares()
        Tiles().create_tiles()

    def draw_squares(self):
        
        x = -15
        y = 105
        
        for i in range(4):
            for j in range(5):
                x += 130
                if x > 700:
                    x = 115
                    y += 130

                arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH, constants.TILE_HEIGHT, arcade.color.SALMON, 5)
        
        arcade.finish_render()

    def on_mouse_press(self, x, y, button, modifiers):

        # get row and column
        column = CheckMatch().get_column(x)
        row = CheckMatch().get_row(y)
        
        # access the sprite in that location
        tile = CheckMatch().get_tile(x, y)
        print(column, x, row, y)
        
        # if there's only 0 or 1 tiles flipped:
            # show tile
            # check if it's a match
            # deal with that ^

