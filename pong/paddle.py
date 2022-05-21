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

from global import *  # Takes in values from the global constants
import arcade  # Gives the class the ability to make objects
from point import Point

"""
* This class will mimic the Pong game and create
* a paddle that can move up and down the y axis
* within the set boundaries.
"""


class Paddle:

    def __init__(self):
        self.center = Point()
        self.center.y = SCREEN_HEIGHT - 150
        self.center.x = SCREEN_WIDTH - 10

    """
    * Creates the paddle from an imported specific
    * class function.
    """

    def draw(self):

        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.BLUE)

    """
    * Controls the paddle by setting the boundaries
    * so it does not move past the SCREEN_HEIGHT.
    """

    def move_up(self):

        if self.center.y < SCREEN_HEIGHT - (PADDLE_HEIGHT / 2):
            # Increases the paddles speed based on the location of the paddle
            self.center.y += MOVE_AMOUNT

    """
    * Controls the paddle by setting the boundaries
    * so it does not move past the bottom of the screen.
    """

    def move_down(self):

        if self.center.y >= PADDLE_HEIGHT / 2:  # Paddle will move halfway past the screen without being divide by
            self.center.y -= MOVE_AMOUNT
