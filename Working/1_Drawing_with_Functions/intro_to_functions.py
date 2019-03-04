import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    arcade.draw_circle_filled(300, 330, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(250, 290, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(325, 290, 50, arcade.color.WHITE)

    arcade.draw_circle_filled(350, 330, 55, arcade.color.GREEN)
    arcade.draw_circle_filled(300, 290, 55, arcade.color.GREEN)
    arcade.draw_circle_filled(375, 290, 55, arcade.color.GREEN)
    arcade.draw_rectangle_filled(350, 360, 50, )

   # call your draw functions

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()