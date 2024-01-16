import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("15/apple.png")
        self.score_value = 1
        self.init_position(game)

    def init_position(self, game):
        self.width = 30
        self.height = 30
        self.center_x = random.randint(20, game.width - 20)
        self.center_y = random.randint(20, game.height - 20)
        self.change_x = 0
        self.change_y = 0

class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__("15/pear.png")
        self.score_value = 2
        self.init_position(game)

    def init_position(self, game):
        self.width = 30
        self.height = 30
        self.center_x = random.randint(20, game.width - 20)
        self.center_y = random.randint(20, game.height - 20)
        self.change_x = 0
        self.change_y = 0

class Poop(arcade.Sprite):
    def __init__(self, game):
        super().__init__("15/poop.png")
        self.score_value = -1
        self.init_position(game)

    def init_position(self, game):
        self.width = 30
        self.height = 30
        self.center_x = random.randint(20, game.width - 20)
        self.center_y = random.randint(20, game.height - 20)
        self.change_x = 0
        self.change_y = 0

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x,
            self.center_y,
            self.width,
            self.height,
            self.color)
        for part in self.body:
            arcade.draw_rectangle_filled(
                part['x'],
                part['y'],
                self.width,
                self.height,
                self.color)

    def move(self):
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food, game):
        self.score += food.score_value
        print("Score:", self.score)
        food.init_position(game)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.food_list = [Apple(self), Pear(self), Poop(self)]

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()

        for food in self.food_list:
            food.draw()

        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

    def on_update(self, delta_time: float):
        self.snake.move()

        for food in self.food_list:
            if arcade.check_for_collision(self.snake, food):
                self.snake.eat(food, self)

if __name__ == "__main__":
    game = Game()
    arcade.run()
