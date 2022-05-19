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
    is hit it will then split into two medium asteroids
    and one small asteroid.
                     
"""

import arcade
import random
from global_ import *
from asteroid import Asteroid
from medium_asteroid import MediumAsteroid
from small_asteroid import SmallAsteroid

"""
* This class will inherit properties from the asteroid
* abstract class and be used as the head of a weak
* inheritance chain.
"""
class LargeAsteroid(Asteroid):

    def __init__(self):
        super().__init__()
        self.center.y = random.uniform(250, SCREEN_HEIGHT - 40)
        self.center.x = random.uniform(100, SCREEN_WIDTH - 50)
        self.rotation = BIG_ROCK_SPIN
        self.radius = BIG_ROCK_RADIUS 

    """
    * Creates the object of a large asteroid through an
    * inported image from the users data file.
    """
    def draw(self):
        img = "meteorGrey_big1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
        
    """
    * Once the asteroid is hit it will then be split into
    * two medium asteroids and one small asteroid. 
    """    
    def hit(self):
        
        self.alive = False
        
        medium1 = MediumAsteroid(self)
        medium1.velocity.dy = self.velocity.dy + 2
        
        medium2 = MediumAsteroid(self)
        medium2.velocity.dy = self.velocity.dy - 2
        
        small1 = SmallAsteroid(self)
        small1.velocity.dx = self.velocity.dx + 5
        
        return [medium1, medium2, small1]
    
 
    """
    * Overiding the flyingObjects advance function to
    * give the asteroids the ability to rotate based
    * on the asteroids angle. 
    """  
    def advance(self):
        self.angle += self.rotation
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

          