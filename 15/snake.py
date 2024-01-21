import arcade
from math import dist

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
        self.size = 0
        self.body = []
        self.coler_num = 0
        self.body_num = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, 
            self.center_y, 
            self.width, 
            self.height, 
            self.color)
        
        for part in range(len(self.body)):
            if part % 3 == 0:
                arcade.draw_rectangle_filled(self.body[part]['x'],
                                             self.body[part]['y'],
                                             self.width,
                                             self.height,
                                             arcade.color.YELLOW)
            else:
                arcade.draw_rectangle_filled(self.body[part]['x'],
                                             self.body[part]['y'],
                                             self.width,
                                             self.height,
                                             self.color)
    
    def move(self):
        self.body.append({'x':self.center_x, 'y':self.center_y})
        
        if len(self.body) > self.size:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, food):
        self.score += food.score
        self.size += food.size
        del food

    def find_best_direction(self, target_x, target_y):
        possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distances = []

        for move in possible_moves:
            new_x = self.center_x + move[0] * self.speed
            new_y = self.center_y + move[1] * self.speed
            distances.append(dist((new_x, new_y), (target_x, target_y)))

        best_move = possible_moves[distances.index(min(distances))]
        return best_move

    def move_towards_food(self, food_list):
        distances = []

        for food in food_list:
            target_x, target_y = food.center_x, food.center_y
            distances.append(dist((self.center_x, self.center_y), (target_x, target_y)))

        if distances:
            closest_food = food_list[distances.index(min(distances))]
            target_x, target_y = closest_food.center_x, closest_food.center_y
            direction = self.find_best_direction(target_x, target_y)

            self.change_x, self.change_y = direction
            self.move()
