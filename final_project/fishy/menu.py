# """
# This is the file designed to pull up both the Start Menu and the Game Over Menu.
# """

# import arcade

# class MenuView(arcade.View):
#     """ Class that manages the 'menu' view"""

#     def on_show(self):
#         """ Called when switching to this view"""
#         """ This is run once when we switch to this view """
#         arcade.set_background_color(arcade.csscolor.WHITE)
#         SCREEN_WIDTH = 800
#         SCREEN_HEIGHT = 600

#         # Reset the viewport, necessary if we have a scrolling game and we need
#         # to reset the viewport back to the start so we can see what we draw.
#         arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

#     def on_draw(self):
#         """ Draw the menu """
#         arcade.start_render()
#         arcade.draw_text("Welcome to Fishy! \n\n", SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=35, anchor_y = "top", anchor_x ="center")
#         arcade.draw_text("Move your fish with WASD, eat the smaller fish to grow, avoid the bigger fish or you'll die. Click anywhere to start.", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, font_size=15, anchor_y = "center", anchor_x="center")

#     def on_mouse_press(self, _x, _y, _button, _modifiers):
#         """ Use a mouse press to advance to the 'game' view"""
#         # game_view = MyGame()
#         # game_view.setup()
#         # self.window.show_view(game_view)
#         return


# class GameOverView(arcade.View):
#     """ Class to manage the game over view"""

#     def on_show(self):
#         """ Called when switching to this view"""

#         arcade.set_background_color(arcade.color.BLACK)

#     def on_draw(self):
#         """ Draw the game over view """

#         arcade.start_render()
#         arcade.draw_text("Game Over - press ENTER to Restart, ESCAPE to Exit", SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5, arcade.color.WHITE, font_size=30, anchor_y = "top", anchor_x="center")

#     def on_key_press(self, key, _modifiers):
#         """ If user hits enter, go back to the main menu view, or quit if escape is hit"""

#         if key == arcade.key.ENTER:
#             menu_view = MenuView()
#             self.window.show_view(menu_view)
#         elif key == arcade.key.ESCAPE:
#             quit()