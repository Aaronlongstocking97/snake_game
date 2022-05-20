"""
 Program:
    CS241 Assignment 05, Re-Create the Pong Game
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program controls the Pong game by mimicking the
    main function. It will activate multiples classes to
    simulate the games design and display to the user
    a window that can be interacted with.
                     
"""
import arcade  # Gives the class the ability to make objects

from global_p import *  # Takes in values from the global constants
from fruit import Fruit
from paddle import Paddle


class Pong(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Fruit
        Paddle
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class,
    but should not have to if you don't want to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.fruit = Fruit()
        self.paddle = Paddle()
        self.score = 0

        # These are used to see if the user is
        # holding down the arrow keys
        self.holding_down = False
        self.holding_up = False
        self.holding_left = False
        self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.fruit.draw()
        self.paddle.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y,
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        # Move the fruit forward one element in time
        # self.fruit.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for fruit at important places
        self.check_miss()
        self.check_hit()
        # self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the fruit has hit the paddle
        and if so, calls its bounce method.
        :return:
        """
        too_close_x = (PADDLE_WIDTH / 2) + FRUIT_RADIUS
        too_close_y = (PADDLE_HEIGHT / 2) + FRUIT_RADIUS

        if (abs(self.fruit.center.x - self.paddle.center.x) < too_close_x and
            abs(self.fruit.center.y - self.paddle.center.y) < too_close_y and
                self.fruit.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            # self.fruit.bounce_horizontal()
            self.score += SCORE_HIT

    def check_miss(self):
        """
        Checks to see if the fruit went past the paddle
        and if so, restarts it.
        """
        if self.fruit.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.fruit.restart()

    # def check_bounce(self):
    #     """
    #     Checks to see if the fruit has hit the borders
    #     of the screen and if so, calls its bounce methods.
    #     """
    #     if self.fruit.center.x < 0 and self.fruit.velocity.dx < 0:
    #         self.fruit.bounce_horizontal()

    #     if self.fruit.center.y < 0 and self.fruit.velocity.dy < 0:
    #         self.fruit.bounce_vertical()

    #     if self.fruit.center.y > SCREEN_HEIGHT and self.fruit.velocity.dy > 0:
    #         self.fruit.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_up:
            self.paddle.move_down()

        if self.holding_down:
            self.paddle.move_up()

        if self.holding_left:
            self.paddle.move_left()

        if self.holding_right:
            self.paddle.move_right()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """

        if key == arcade.key.UP:
            self.holding_right = True

        if key == arcade.key.DOWN:
            self.holding_right = True

        if key == arcade.key.LEFT:
            self.holding_left = True

        if key == arcade.key.RIGHT:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """

        if key == arcade.key.UP:
            self.holding_right = False

        if key == arcade.key.DOWN:
            self.holding_right = False

        if key == arcade.key.LEFT:
            self.holding_left = False

        if key == arcade.key.RIGHT:
            self.holding_right = False


window = Pong(SCREEN_WIDTH, SCREEN_HEIGHT)  # creates the game window
arcade.run()  # Starts the actions listed to run the game
