"""
 Program:
    CS241 Assignment 05, Re-Create the Pong Game
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will create a virtual fruit that
    will bounce based on the x and y axis as well
    as the velocity given. The fruit will stay in
    the boundaries of the window, but will have
    the ability to move past the right side of the
    screen. 
                     
"""
import random
from global_p import *
import arcade
from point_p import Point
# from velocity_p import Velocity

"""
* This class will take in values from multiple
* classes to draw, guide, and increase/decrease
* the speed of the virtual fruit.
"""


class Fruit:

    def __init__(self):

        self.center = Point()
        # self.velocity = Velocity()
        self.restart()

    """
    * Creates the virtual fruit from an imported arcade class.
    """

    def draw(self):

        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, FRUIT_WIDTH, FRUIT_HEIGHT, arcade.color.RED)

    """
    * Controls the fruits movement within the window.
    """

    # def advance(self):

    #     self.center.x += self.velocity.dx
    #     self.center.y += self.velocity.dy

    """
    * The fruit will move forward or backward based
    * on the velocity of the fruit.
    """

    # def bounce_horizontal(self):

    #     self.velocity.dx *= -1
    #     #self.velocity.dx = self.velocity.dx * -1

    """
    * The fruit will move up or down based
    * on the velocity of the fruit.
    """

    # def bounce_vertical(self):

    #     self.velocity.dy *= -1  # If the fruit moves to close to the
    #     # boundaries it will then change direction.

    """
    * Recreates the fruit at the starting point for the
    * given x and random y axis'. Values are initalized
    * at this function instead because the values are
    * already given in the pr-existing classes.
    """

    def restart(self):
        self.center.y = random.uniform(50, SCREEN_HEIGHT - 50)
        self.center.x = random.uniform(50, SCREEN_WIDTH - 50)
        # uniform gives the values listed
        # self.velocity.dx = random.uniform(2, 6)
        # self.velocity.dy = random.uniform(2, 5)  # a floating point #
