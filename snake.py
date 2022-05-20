"""
 Program:
    CS241 Assignment 05, Re-Create the Pong Game
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will implement an object from the
    imported arcade class. This object will move within
    the boundaries set by the y axis and move up and down. 
                     
"""

from global_p import *  # Takes in values from the global constants
import arcade  # Gives the class the ability to make objects
from point_p import Point

"""
* This class will mimic the Pong game and create
* a snake that can move up and down the y axis
* within the set boundaries.
"""


class Snake:

    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 150
        self.center.x = SCREEN_WIDTH - 10

    """
    * Creates the snake from an imported specific
    * class function.
    """

    def draw(self):

        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, SNAKE_WIDTH, SNAKE_HEIGHT, arcade.color.BLUE)

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the SCREEN_HEIGHT.
    """

    def move_up(self):

        if self.center.y < SCREEN_HEIGHT - (SNAKE_HEIGHT / 2):
            # Increases the snakes speed based on the location of the snake
            self.center.y += MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_down(self):

        if self.center.y >= SNAKE_HEIGHT / 2:  # Snake will move halfway past the screen without being divide by
            self.center.y -= MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_left(self):

        if self.center.x >= SNAKE_WIDTH:  # Snake will move halfway past the screen without being divide by
            self.center.x -= MOVE_AMOUNT

    """
    * Controls the snake by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_right(self):

        if self.center.x < SCREEN_WIDTH - (SNAKE_WIDTH / 2):
            # Increases the snakes speed based on the location of the snake
            self.center.x += MOVE_AMOUNT
