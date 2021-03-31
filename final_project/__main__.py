"""
Platformer Game
"""
import arcade
import random

from arcade.application import MOUSE_BUTTON_LEFT, View
from fishy import constants
# from fishy import menu
# from fishy import computer_fish
# from fishy.player_sprite import PlayerSprite

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


class MenuView(arcade.View):
    """ Class that manages the 'menu' view"""

    def on_show(self):
        """ Called when switching to this view"""
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.WHITE)
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to Fishy! \n\n", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=35, anchor_y = "top", anchor_x ="center")
        arcade.draw_text("Move your fish with WASD, eat the smaller fish to grow, avoid the bigger fish or you'll die. Click anywhere to start.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=15, anchor_y = "center", anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view"""
        game_view = MyGame(arcade.View, self)
        game_view.setup()
        self.window.show_view(game_view)

class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(player_sprite, computer_list, self):

        # Call the parent class and set up the window
        # super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        super().__init__()
        # window = menu.MenuView(self)

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

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.computer_list)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.computer_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()
        self.collided_sprites = self.physics_engine.update()
        for sprite in self.collided_sprites:
            player_size = self.player_sprite._get_scale()
            if sprite._get_scale() >= player_size:
                GameOverView(self)
            else:
                self.computer_list.remove(sprite)

class GameOverView(arcade.View):
    """ Class to manage the game over view"""

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """

        arcade.start_render()
        arcade.draw_text("Game Over - press ENTER to Restart, ESCAPE to Exit", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/1.5, arcade.color.WHITE, font_size=30, anchor_y = "top", anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits enter, go back to the main menu view, or quit if escape is hit"""

        if key == arcade.key.ENTER:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        elif key == arcade.key.ESCAPE:
            quit()

def main():
    """ Main method """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()