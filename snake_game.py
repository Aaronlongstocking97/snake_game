"""
 Program:
    Snake PyGame - A 2D Snake Game
 Author:
    Aaron Jones
 Summary: 
    This program controls the Snake game by mimicking the
    main function. It will activate multiples classes to
    simulate the games design and display to the user
    a window that can be interacted with.
                     
"""
import arcade  # Gives the class the ability to make objects
from settings import *  # Takes in values from the global constants
from food import Food
from snake import Snake


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Point
        Velocity
        Food
        Snake
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

        self.food = Food()
        self.snake = Snake()
        self.score = 0
        self.held_keys = set()

        # These are used to see if the user is
        # holding down the arrow keys
        # self.holding_down = False
        # self.holding_up = False
        # self.holding_left = False
        # self.holding_right = False

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.food.draw()
        # self.snake.draw()
        if self.snake.alive == True:
            self.snake.draw()

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

        # Move the food forward one element in time
        # self.food.advance()

        # Check to see if keys are being held, and then
        # take appropriate action
        self.check_keys()

        # check for food at important places
        self.check_miss()
        self.check_hit()
        # self.check_bounce()

    def check_hit(self):
        """
        Checks to see if the food has hit the snake
        and if so, calls its bounce method.
        :return:
        """

        too_close_x = (SNAKE_WIDTH / 2) + FOOD_WIDTH
        too_close_y = (SNAKE_HEIGHT / 2) + FOOD_HEIGHT

        if (abs(self.food.center.x - self.snake.center.x) < too_close_x and
            abs(self.food.center.y - self.snake.center.y) < too_close_y and
                self.food.velocity.dx > 0):
            # we are too close and moving right, this is a hit!
            # self.food.bounce_horizontal()
            self.score += SCORE_HIT
            self.snake.alive = False

    def check_miss(self):
        """
        Checks to see if the food went past the snake
        and if so, restarts it.
        """
        if self.food.center.x > SCREEN_WIDTH:
            # We missed!
            self.score -= SCORE_MISS
            self.food.restart()

    # def check_bounce(self):
    #     """
    #     Checks to see if the food has hit the borders
    #     of the screen and if so, calls its bounce methods.
    #     """
    #     if self.food.center.x < 0 and self.food.velocity.dx < 0:
    #         self.food.bounce_horizontal()

    #     if self.food.center.y < 0 and self.food.velocity.dy < 0:
    #         self.food.bounce_vertical()

    #     if self.food.center.y > SCREEN_HEIGHT and self.food.velocity.dy > 0:
    #         self.food.bounce_vertical()

    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if arcade.key.UP in self.held_keys:
            self.snake.move_up()

        if arcade.key.DOWN in self.held_keys:
            self.snake.move_down()

        if arcade.key.LEFT in self.held_keys:
            self.snake.move_left()

        if arcade.key.RIGHT in self.held_keys:
            self.snake.move_right()

        # if self.holding_up:
        #     self.snake.move_up()

        # if self.holding_down:
        #     self.snake.move_down()

        # if self.holding_left:
        #     self.snake.move_left()

        # if self.holding_right:
        #     self.snake.move_right()

    def on_key_press(self, key: int, modifiers: int):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if self.snake.alive:
            self.held_keys.add(key)

        # if key == arcade.key.UP:
        #     self.holding_up = True

        # if key == arcade.key.DOWN:
        #     self.holding_down = True

        # if key == arcade.key.LEFT:
        #     self.holding_left = True

        # if key == arcade.key.RIGHT:
        #     self.holding_right = True

    def on_key_release(self, key: int, modifiers: int):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

        # if key == arcade.key.UP:
        #     self.holding_up = False

        # if key == arcade.key.DOWN:
        #     self.holding_down = False

        # if key == arcade.key.LEFT:
        #     self.holding_left = False

        # if key == arcade.key.RIGHT:
        #     self.holding_right = False


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)  # creates the game window
arcade.run()  # Starts the actions listed to run the game
