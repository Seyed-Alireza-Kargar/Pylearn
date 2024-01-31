import arcade

class Ball(arcade.Sprite) :
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.YELLOW
        self.radius = 15
        self.change_x = 0
        self.change_y = 0
        self.speed = 3

    def move(self):
        ...
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y,
                                  self.radius, self.color)

class Rocket(arcade.Sprite):
    def __init__(self, x, y, c, n):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.name = n
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 60
        self.speed = 4
        self.scor = 0

    def move(self):
        ...
    
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y,
                                     self.width, self.height, self.color)

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=500, title="Pong 2024 🏓")
        arcade.set_background_color(arcade.color.DARK_GREEN)
        self.player_1 = Rocket(40, self.height // 2, arcade.color.RED, "Alireza")
        self.player_2 = Rocket(self.width - 40, self.height // 2, arcade.color.CYAN, "Mammad")
        self.ball = Ball(self)



    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_outline(self.width // 2, self.height // 2,
                                      self.width - 10, self.height - 10,
                                      arcade.color.WHITE, border_width=10)
        arcade.draw_line(self.width // 2, 10, self.width // 2, self.height - 10,
                        color=arcade.color.WHITE, line_width=10)
        
        self.player_1.draw()
        self.player_2.draw()
        self.ball.draw()
        arcade.finish_render()
         

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        # self.player_1.center_x = x
        if self.player_1.height - 15 < y < self.height - self.player_1.height + 15:
            self.player_1.center_y = y

    

game = Game()
arcade.run()