import arcade
from fishy.menu import GameOverView

class PlayerSprite:
    def __init__(self):
        self.sprite = None

    def set_image(self, image_source, scaling):
        self.sprite = arcade.Sprite(image_source, scaling)

    def set_position(self, x, y):
        self.sprite.center_x = x
        self.sprite.center_y = y