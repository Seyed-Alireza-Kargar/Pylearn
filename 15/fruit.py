import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self, game, png):
        super().__init__(png)
        self.width = 30
        self.height = 30
        self.center_x = random.randint(10, game.width - 20)
        self.center_y = random.randint(10, game.height - 20)
        self.score = 0
        self.size = 0

class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game, "15/apple.png")
        self.score = 1
        self.size = 1


class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game, '15/pear.png')
        self.score = 2

class Poo(Fruit):
    def __init__(self, game):
        super().__init__(game, '15/poop.png')
        self.score = -1