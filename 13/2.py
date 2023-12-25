import arcade

class PatternGenerator(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width=width, height=height, title=title)
        self.pattern_size = 30
        self.RED = arcade.color.RED
        self.BLUE = arcade.color.BLUE

    def draw_shape(self, x, y, color):
        arcade.draw_ellipse_filled(x, y, self.pattern_size // 2, self.pattern_size // 2, color)

    def on_draw(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()

        for i in range(0, self.width, self.pattern_size):
            for j in range(0, self.height, self.pattern_size):
                color = self.RED if (i // self.pattern_size % 2 == j // self.pattern_size % 2) else self.BLUE
                self.draw_shape(i + self.pattern_size, j + self.pattern_size, color)

def main():
    generator = PatternGenerator(500, 500, "Pattern Generator")
    arcade.run()

if __name__ == "__main__":
    main()
