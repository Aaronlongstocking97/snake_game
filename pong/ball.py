"""
 Program:
    CS241 Assignment 05, Re-Create the Pong Game
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will create a virtual ball that
    will bounce based on the x and y axis as well
    as the velocity given. The ball will stay in
    the boundaries of the window, but will have
    the ability to move past the right side of the
    screen. 
                     
"""
import random
from global_ import *
import arcade
from point import Point
from velocity import Velocity

"""
* This class will take in values from multiple
* classes to draw, guide, and increase/decrease
* the speed of the virtual ball.
"""


class Ball:

    def __init__(self):

        self.center = Point()
        self.velocity = Velocity()
        self.restart()

    """
    * Creates the virtual ball from an imported arcade class.
    """

    def draw(self):

        arcade.draw_circle_filled(
            self.center.x, self.center.y, BALL_RADIUS, arcade.color.RED)

    """
    * Controls the balls movement within the window.
    """

    def advance(self):

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    """
    * The ball will move forward or backward based
    * on the velocity of the ball.
    """

    def bounce_horizontal(self):

        self.velocity.dx *= -1
        #self.velocity.dx = self.velocity.dx * -1

    """
    * The ball will move up or down based
    * on the velocity of the ball.
    """

    def bounce_vertical(self):

        self.velocity.dy *= -1  # If the ball moves to close to the
        # boundaries it will then change direction.

    """
    * Recreates the ball at the starting point for the
    * given x and random y axis'. Values are initalized
    * at this function instead because the values are
    * already given in the pr-existing classes.
    """

    def restart(self):
        self.center.y = random.uniform(5, SCREEN_HEIGHT - 5)
        self.center.x = 10
        # uniform gives the values listed
        self.velocity.dx = random.uniform(2, 6)
        self.velocity.dy = random.uniform(2, 5)  # a floating point #
