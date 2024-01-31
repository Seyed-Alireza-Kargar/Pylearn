import arcade

class Heart(arcade.Sprite):
    def __init__(self, x):
        super().__init__(":resources:images/items/gemRed.png")
        self.center_x = x * 25
        self.center_y = 10
        self.width = 45
        self.height = 45