import random
import arcade
import os
from game.tile import Tile
from game import constants

class Tiles():
    def __init__(self):
        self.images = ['abacus', 'watch', 'healthy', 'scooter' ,'reindeer', 'robot', 'rocket', 'science', 'gameboy', 'whale']
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.sprite_list = arcade.SpriteList()

    def create_tiles(self):
        for image in self.images:
            for i in range(2):
                spot = random.choice(self.positions)
                x = self.get_x(spot)
                y = self.get_y(spot)
                self.positions.pop(self.positions.index(spot))

                sprite = self.sprite_list.append(Tile(image, scale=0.1, center_x=x, center_y=y, spot= spot))
                arcade.draw_rectangle_outline(x, y, constants.TILE_WIDTH -5, constants.TILE_HEIGHT -5, arcade.color.SALMON, 5)
        # print(self.sprite_list)
        self.sprite_list.draw()
        arcade.finish_render()

    def get_x(self, position):
        if position in (1, 6, 11, 16):
            return 115
        elif position in (2, 7, 12, 17):
            return 245 
        elif position in (3, 8, 13, 18):
            return 375 
        elif position in (4, 9, 14, 19):
            return 505 
        elif position in (5, 10, 15, 20):
            return 635 

    def get_y(self, position):
        if position in (1, 2, 3, 4, 5):
            return 105
        elif position in (6, 7, 8, 9, 10):
            return 235
        elif position in (11, 12, 13, 14, 15):
            return 365         
        elif position in (16, 17, 18, 19, 20):
            return 495

