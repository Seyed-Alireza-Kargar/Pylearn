import random
import arcade

class Invader(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height + 15
        self.width = 60
        self.height = 60 
        self.angle = 180

class Bullet(arcade.Sprite):
    def __init__(self, source, angle, speed):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = source.center_x
        self.center_y = source.center_y
        self.angle = angle
        self.change_y = speed

class Spaceship(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 10
        self.width = 60
        self.height = 60 
        self.speed = 15
        self.bullet_list = arcade.SpriteList()

    def fire_bullet(self):
        bullet = Bullet(self, 90, 5)
        self.bullet_list.append(bullet)

    def update_bullets(self):
        for bullet in self.bullet_list:
            bullet.center_y += bullet.change_y
            if bullet.top < 0:
                self.bullet_list.remove(bullet)

    def draw_bullets(self):
        self.bullet_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.center_x -= self.speed
        elif symbol == arcade.key.D:
            self.center_x += self.speed
        elif symbol == arcade.key.SPACE:
            self.fire_bullet()

    def update(self):
        self.update_bullets()

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=480, height=720, title="Galactic Battle")
        arcade.set_background_color(arcade.color.DARK_VIOLET)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.player = Spaceship(self)
        self.invader = Invader(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)

        self.player.draw()
        self.invader.draw()
        self.player.draw_bullets()

    def on_key_press(self, symbol: int, modifiers: int):
        self.player.on_key_press(symbol, modifiers)

    def on_update(self, delta_time: float):
        self.invader.center_y -= 1
        self.player.update()

def main():
    game_window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
