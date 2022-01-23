import arcade
from game import constants

class StartGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self.first = arcade.SpriteList()
        
    def setup(self):
        arcade.set_background_color(constants.BACKGROUND_COLOR)

        self.first = arcade.Sprite(constants.FIRST)
        self.draw_tiles()


    def draw_tiles(self):
        
        x = 100
        y = 100

        for i in range(4):
            for j in range(4):
                x += 100
                y += 100
                arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH, constants.TILE_HEIGHT, constants.SALMON)