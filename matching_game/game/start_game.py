import arcade
from game import constants

class StartGame(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()


    def on_draw(self):
        arcade.start_render()
        self.draw_tiles()

    def draw_tiles(self):
        
        x = -15
        y = 105
        
        for i in range(4):
            for j in range(5):
                x += 130
                if x > 700:
                    x = 115
                    y += 130

                arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH, constants.TILE_HEIGHT, arcade.color.SALMON, 5)
