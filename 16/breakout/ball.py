import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = 250
        self.center_y = 35 + self.height
        self.change_x = random.choice([1, -1])
        self.change_y = 1
        self.radius = 10
        self.height = self.radius*2
        self.width = self.radius*2
        self.speed = 5
        self.color = arcade.color.GREEN_YELLOW

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)