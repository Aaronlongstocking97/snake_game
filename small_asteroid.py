"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will take in an image which will take
    in the properties of an ansteroid. Once the asteroid
    is hit it will then be taken off the screen through
    a function called CLEAN_UP_ZOMBIES inside of the
    Game class.
                     
"""

import arcade
from global_ import *
from asteroid import Asteroid

"""
* This class will taken in the properties of the
* Medium_asteroid class and will use these properties
* for the position in which the asteroid splits apart
* as well as the velocity the asteroid is traveling at.
"""
class SmallAsteroid(Asteroid):

    def __init__(self, medium_asteroid):
        super().__init__()
        self.center.x = medium_asteroid.center.x
        self.center.y = medium_asteroid.center.y
        self.rotation = SMALL_ROCK_SPIN
        self.radius = SMALL_ROCK_RADIUS

    """
    * Creates the object of a large asteroid through an
    * inported image from the users data file. 
    """
    def draw(self):
        img = "meteorGrey_small1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    """
    * Once the asteroid is hit it will return an
    * empty list and will be taken off screen.
    """
    def hit(self):
        self.alive = False
        
        return []
    
    """
    * Overiding the flyingObjects advance function to
    * give the asteroids the ability to rotate based
    * on the asteroids angle. 
    """  
    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    