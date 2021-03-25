"""
This is the file designed to pull up both the Start Menu and the Game Over Menu.
"""

from fishy import constants
import arcade

class MenuView(arcade.View):
    """ Class that manages the 'menu' view"""

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to Fishy! \n\n", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=35, anchor_y = "top", anchor_x ="center")
        arcade.draw_text("Move your fish with WASD, eat the smaller fish to grow, avoid the bigger fish or you'll die. Click anywhere to start.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=15, anchor_y = "center", anchor_x="center")

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """ Use a mouse press to advance to the 'game' view"""
        return


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
    """ Startup """
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()