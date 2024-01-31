import arcade

class Brik(arcade.Sprite):
    def __init__(self, game, x, y, c):
        super().__init__()
        self.center_x = x*50+((game.width//10)//2)
        self.center_y = y*20 + 250
        self.width = game.width // 10
        self.height = 15
        self.color = c

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)