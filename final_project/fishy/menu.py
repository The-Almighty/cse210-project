"""
Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each View will need to have its own draw,
update and window event methods. To switch a View, simply create a View
with `view = MyView()` and then use the "self.window.set_view(view)" method.
"""

import arcade
from fishy import constants


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    
    def on_show(self):
        """ Called when switching to this view"""
        window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        menu_view = MenuView()
        window.show_view(menu_view)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to Fishy!  Move your fish with WASD, eat the smaller fish to grow, avoid the bigger fish or you'll die. Click anywhere to start.", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=25, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        return


class GameOverView(arcade.View):
    """ Class to manage the game over view """

    def on_show(self):
        """ Called when switching to this view"""

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Draw the game over view """

        arcade.start_render()
        arcade.draw_text("Game Over - press ENTER to Restart, ESCAPE to Exit", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2, arcade.color.WHITE, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the main menu view """

        if key == arcade.key.ENTER:
            menu_view = MenuView()
            self.window.show_view(menu_view)
        elif key == arcade.key.ESCAPE:
            quit()
