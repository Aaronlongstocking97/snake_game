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

    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 450
        self.center.x = SCREEN_WIDTH - 600
        # defining first 4 blocks of snake body
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.snake_position = [self.center.x, self.center.y]

    """
    * Creates the snake from an imported specific
    * class function.
    """

    def draw(self):

        for pos in self.snake_body:
            arcade.draw_rectangle_filled(
                pos[0], pos[1], SNAKE_WIDTH, SNAKE_HEIGHT, arcade.color.BLUE)

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the SCREEN_HEIGHT.
    """

    def move_up(self):
        self.snake_position[1] -= 10

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_down(self):
        self.snake_position[1] += 10

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_left(self):
        self.snake_position[0] -= 10

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_right(self):
        self.snake_position[0] += 10
