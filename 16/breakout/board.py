import arcade

class Board(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = 35
        self.change_x = 0
        self.change_y = 0
        self.width = game.width // 10 + 10
        self.height = 10
        self.color = arcade.color.CYAN
        self.speed = 4
        self.score = 0

    def move(self):
        self.center_x += self.change_x*self.speed

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color) 