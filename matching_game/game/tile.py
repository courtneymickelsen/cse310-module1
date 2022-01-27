import arcade
import os

class Tile(arcade.Sprite):
    def __init__(self, image: str, scale: float, center_x: float, center_y: float, spot: int):
        self.image = image
        self.spot = spot
        self.collision_radius = 50
        self.hit_box = 50
        self.name = 'green'
        self.path = os.path.join(os.getcwd(), f"./matching_game/game/images/{self.name}.png")
        super().__init__(self.path, scale= scale, center_x= center_x, center_y= center_y)


    def get_name(self):
        return self.name

    def flip(self, sprite_list):
        if self.name == 'green':
            self.name = self.image
        elif self.name == self.image:
            self.name = 'green'
        print(self.name)

        self.path = os.path.join(os.getcwd(), f"./matching_game/game/images/{self.name}.png")
        self.update()

        # debugging- the image path is correct
        print(self.path)

        # This is the only thing that wont work, I need it to redraw the list of sprites
        # but they still use the old image... I've tried all kinds of functions and methods 
        # but none of them will work. 
        sprite_list.draw()
        
        arcade.finish_render()



        

