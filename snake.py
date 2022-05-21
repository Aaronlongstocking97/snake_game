"""
 Program:
    Snake PyGame Playable Character
 Author:
    Aaron Jones
 Summary: 
    
                     
"""

from settings import *  # Takes in values from the global constants
import arcade  # Gives the class the ability to make objects
from point import Point

"""
* This class will mimic the Pong game and create
* a snake that can move up and down the y axis
* within the set boundaries.
"""


class Snake:

    def __init__(self, head_pos=[0, 0]):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 590
        self.center.x = SCREEN_WIDTH - 300
        self.alive = True
        self.head_pos = head_pos
        # defining first 4 blocks of snake body
        # self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        # self.snake_position = [self.center.x, self.center.y]

    """
    * Creates the snake from an imported specific
    * class function.
    """

    def draw(self):

        # for pos in self.snake_body:
        #     arcade.draw_rectangle_filled(
        #         pos[0], pos[1], SNAKE_WIDTH, SNAKE_HEIGHT, arcade.color.BLUE)
        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, SNAKE_WIDTH, SNAKE_HEIGHT, arcade.color.GREEN)

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the SCREEN_HEIGHT.
    """

    def move_up(self):
        # self.snake_position[1] -= 10
        self.center.y += MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_down(self):
        # self.snake_position[1] += 10
        self.center.y -= MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_left(self):
        # self.snake_position[0] -= 10
        self.center.x -= MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_right(self):
        # self.snake_position[0] += 10
        self.center.x += MOVE_AMOUNT
