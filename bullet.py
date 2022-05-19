"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program displays to the user a picture that is controlled by
    Game class and represents a bullet being fired. It derives from
    the FlyingObjects class through the use of Inheritance.
                     
"""

import arcade
import math
from global_ import *
from flying_objects import FlyingObjects

"""
* This class will represent a bullet that will be used through
* the Game class and takes in the global variable for the radius.
"""
class Bullet(FlyingObjects):

    def __init__(self, ship):
        super().__init__()
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.age = BULLET_LIFE
        self.angle = ship.angle
        self.radius = BULLET_RADIUS
    
    """
    * Takes in the saved image and displays this as the bullet object
    """
    def draw(self):
        img = "laserBlue01.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
    
    """
    * Overides the advance from the inherited FlyingObjects class
    * and gives the bullet a life span of sixty seconds.
    """
    def advance(self):
        self.age -= 1
        if self.age < 0:
            self.alive = False

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
           
    """
    * Redefines the Velocities that are inherited through the FlyingObjects
    * class and uses the global BULLET_SPEED to calculate the direction of
    * the objects momentum. 
    """
    def fire(self):
        self.velocity.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED
        
            
        
