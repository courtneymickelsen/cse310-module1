import arcade
from game import constants

class StartGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)
        
        arcade.run()

    def setup(self):
        self.draw_tiles()

    def draw_tiles(self):
        
        x = 100
        y = 100

        arcade.start_render()

        arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH, constants.TILE_HEIGHT, constants.SALMON)

        for i in range(4):
            for j in range(4):
                x += 100
                y += 100
                arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH, constants.TILE_HEIGHT, constants.SALMON)
        
        arcade.finish_render()