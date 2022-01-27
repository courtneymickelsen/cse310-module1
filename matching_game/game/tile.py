import arcade
import os

class Tile(arcade.Sprite):
    def __init__(self, image: str, scale: float, center_x: float, center_y: float, spot: int):
        self.image = f'{image}'
        self.spot = spot
        self.collision_radius = 50
        self.hit_box = 50
        self.name = 'green'
        # self.collides_with_point
        self.path = os.path.join(os.getcwd(), f"./matching_game/game/images/{self.name}.png")
        # self.sprite_list = arcade.SpriteList(use_spatial_hash= True)
        super().__init__(self.path, scale= scale, center_x= center_x, center_y= center_y, hit_box_detail= 50)

    def get_name(self):
        return self.name

    def flip(self, sprite_list):
        if self.name == 'green':
            self.name = self.image
            self.path = self.path.replace(f'{os.path.join(os.getcwd(), f"./matching_game/game/images/{self.name}.png")}', f'{os.path.join(os.getcwd(), f"./matching_game/game/images/{self.image}.png")}')
            print(self.name)
        elif self.name == self.image:
            self.name = 'green'
        arcade.start_render()
        self.draw()
        arcade.finish_render()


        

