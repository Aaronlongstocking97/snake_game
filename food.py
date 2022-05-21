"""
 Program:
    Snake PyGame Food Object
 Author:
    Aaron Jones
 Summary: 
    
                     
"""
import random
from settings import *
import arcade
from point import Point
# from velocity_p import Velocity

"""
* This class will take in values from multiple
* classes to draw, guide, and increase/decrease
* the speed of the virtual food.
"""


class Food:

    def __init__(self):

        self.center = Point()
        # self.velocity = Velocity()
        self.restart()

    """
    * Creates the virtual food from an imported arcade class.
    """

    def draw(self):

        arcade.draw_rectangle_filled(
            self.center.x, self.center.y, FOOD_WIDTH, FOOD_HEIGHT, arcade.color.RED)

    """
    * Controls the foods movement within the window.
    """

    # def advance(self):

    #     self.center.x += self.velocity.dx
    #     self.center.y += self.velocity.dy

    """
    * The food will move forward or backward based
    * on the velocity of the food.
    """

    # def bounce_horizontal(self):

    #     self.velocity.dx *= -1
    #     #self.velocity.dx = self.velocity.dx * -1

    """
    * The food will move up or down based
    * on the velocity of the food.
    """

    # def bounce_vertical(self):

    #     self.velocity.dy *= -1  # If the food moves to close to the
    #     # boundaries it will then change direction.

    """
    * Recreates the food at the starting point for the
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
