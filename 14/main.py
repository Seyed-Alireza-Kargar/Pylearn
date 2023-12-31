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
        self.can_move = True

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
        self.speed = 10
        self.bullet_list = arcade.SpriteList()

        self.lives = 3
        self.score = 0
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.shoot_sound = arcade.load_sound(":resources:sounds/laser1.wav")

    def move_left(self):
        self.change_x = -self.speed

    def move_right(self):
        self.change_x = self.speed

    def stop_moving(self):
        self.change_x = 0

    def fire_bullet(self):
        bullet = Bullet(self, 90, 5)
        self.bullet_list.append(bullet)
        arcade.play_sound(self.shoot_sound)

    def update_bullets(self):
        for bullet in self.bullet_list:
            bullet.center_y += bullet.change_y
            if bullet.top < 0:
                self.bullet_list.remove(bullet)

    def draw_bullets(self):
        self.bullet_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.move_left()
        elif key == arcade.key.D:
            self.move_right()
        elif key == arcade.key.SPACE:
            self.fire_bullet()

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.A, arcade.key.D]:
            self.stop_moving()

    def update(self):
        super().update()
        self.update_bullets()

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=480, height=720, title="Galactic Battle")
        arcade.set_background_color(arcade.color.DARK_VIOLET)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.player = Spaceship(self)
        self.invader_list = arcade.SpriteList()
        self.enemy_spawn_timer = 0
        self.enemy_spawn_interval = 3
        self.enemy_speed = 1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.player.draw()
        self.player.draw_bullets()
        self.invader_list.draw()
        arcade.draw_text(f"♥️ {self.player.lives}", 10, 10, arcade.color.WHITE, 14)
        arcade.draw_text(f"Score: {self.player.score}", self.width - 100, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time: float):
        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer >= self.enemy_spawn_interval:
            self.enemy_spawn_timer = 0
            invader = Invader(self)
            invader.speed = self.enemy_speed
            self.invader_list.append(invader)
            self.enemy_speed += 0.1

        for bullet in self.player.bullet_list:
            for invader in self.invader_list:
                if bullet.collides_with_sprite(invader):
                    self.player.bullet_list.remove(bullet)
                    self.invader_list.remove(invader)
                    self.player.score += 1
                    arcade.play_sound(self.player.explosion_sound)

        for invader in self.invader_list:
            if invader.center_y < self.player.center_y:
                self.player.lives -= 1
                self.invader_list.remove(invader)

        if self.player.lives <= 0:
            arcade.draw_text("GAME OVER", self.width // 2 - 100, self.height // 2, arcade.color.WHITE, 24)
            arcade.pause(1)
            arcade.close_window()

        self.player.update()
        for invader in self.invader_list:
            invader.center_y -= invader.speed

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

def main():
    game_window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()
