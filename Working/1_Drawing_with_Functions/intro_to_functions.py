import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions




def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.BLUE)
    arcade.start_render()

def cloud(x,y,z):
    arcade.draw_circle_filled(x - 200, 530, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 150, 490, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x -225, 490, 50, arcade.color.WHITE)

def treebase(a,b,c,d):
    arcade.draw_rectangle_filled(a - 100,b - 100, c - 100, , 150,
                                 arcade.color.BRITISH_RACING_GREEN, 0)

def treeleaves(e,f,g):
    arcade.draw_circle_filled(555, 330, 60, arcade.color.GREEN_YELLOW)
    arcade.draw_circle_filled(505, 290, 60, arcade.color.GREEN_YELLOW)
    arcade.draw_circle_filled(580, 290, 60, arcade.color.GREEN_YELLOW)

    arcade.draw_circle_filled(120, 2, 200, arcade.color.BOTTLE_GREEN)
    arcade.draw_circle_filled(800, 2, 200, arcade.color.BOTTLE_GREEN)
    arcade.draw_circle_filled(450, 2, 200, arcade.color.BOTTLE_GREEN)


   # call your draw functions

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()

cloud(300, 530, 50)
cloud(250, 490, 50)
could(325, 490, 50)
treebase(550, 178, 60, 150)
treeleaves(555, 330, 60)
treeleaves(505, 290, 60)
treeleaves(580, 290, 60)
