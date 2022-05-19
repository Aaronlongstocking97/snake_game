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
    is hit it will then split into two small asteroids.
                     
"""

import arcade
from global_ import *
from asteroid import Asteroid
from small_asteroid import SmallAsteroid

"""
* This class will taken in the properties of the
* Large_asteroid class and will use these properties
* for the position in which the asteroid splits apart
* as well as the velocity the asteroid is traveling at.
"""
class MediumAsteroid(Asteroid):

    def __init__(self, large_asteroid):
        super().__init__()
        self.center.x = large_asteroid.center.x
        self.center.y = large_asteroid.center.y
        self.rotation = MEDIUM_ROCK_SPIN
        self.radius = MEDIUM_ROCK_RADIUS
    """
    * Creates the object of a large asteroid through an
    * inported image from the users data file.
    """
    def draw(self):  
        img = "meteorGrey_med1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    """
    * Once the asteroid is hit it will then split into two small
    * asteroids that will have an inherted velocity from the
    * Medium_asteroid class. 
    """
    def hit(self):
        
        self.alive = False
        
        small2 = SmallAsteroid(self)
        small2.velocity.dy = self.velocity.dy + 1.5
        small2.velocity.dx = self.velocity.dx + 1.5
        
        small3 = SmallAsteroid(self)
        small3.velocity.dy = self.velocity.dy - 1.5
        small3.velocity.dx = self.velocity.dx - 1.5
        
        return [small2, small3]
    
    """
    * Overiding the flyingObjects advance function to
    * give the asteroids the ability to rotate based
    * on the asteroids angle. 
    """  
    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
  
