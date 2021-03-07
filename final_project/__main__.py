"""
Platformer Game
"""
import arcade
import random
from fishy import constants
from fishy.player_sprite import PlayerSprite

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.computer_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.computer_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/enemies/fishGreen.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = constants.SCREEN_WIDTH / 2
        self.player_sprite.center_y = constants.SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        coordinate_list = [[constants.SCREEN_WIDTH - 10, random.randint(0, constants.SCREEN_HEIGHT)],
                           [constants.SCREEN_WIDTH - 10, random.randint(0, constants.SCREEN_HEIGHT)],
                           [constants.SCREEN_WIDTH - 10, random.randint(0, constants.SCREEN_HEIGHT)]]

        for coordinate in coordinate_list:
            # Add a computer fish on the side of the screen
            wall = arcade.Sprite(":resources:images/enemies/fishPink.png", TILE_SCALING)
            wall.position = coordinate
            self.computer_list.append(wall)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.computer_list.draw()
        self.player_list.draw()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()