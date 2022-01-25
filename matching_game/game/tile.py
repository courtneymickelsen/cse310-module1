import arcade
import os 

class Tile(arcade.Sprite):
    def __init__(self, image: str, scale: float, center_x: float, center_y: float, spot: int):
        self.spot = spot
        self.name = image
        self.path = os.path.join(os.getcwd(), f"./matching_game/game/images/{image}.png")
        
        super().__init__(self.path, scale, center_x= center_x, center_y= center_y, hit_box_algorithm="None")

    def get_name(self):
        return self.name