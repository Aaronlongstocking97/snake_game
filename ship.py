"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary:
    This program will inherit properties from the FlyingObjects class
    as well as set the angle thats defined in the member variable to
    create the object that mimics the ability to act like a ship. It
    will take in control keys that will give the ship the ability to
    move as well as a fire funciton that will work with the bullet
    class through a weak inheritance. 
            
"""

import math
import arcade
from global_ import *
from flying_objects import FlyingObjects

"""
* This class will redifine the position of the ship
* as well as change the angle and velocity that the
* ship is traveling on. 
"""
class Ship(FlyingObjects):

    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.speed = SHIP_THRUST_AMOUNT
        self.angle = 90
        self.radius = SHIP_RADIUS
    

    """
    * Creates the ship based on an imported image which takes on
    * multiple controls.
    """
    def draw(self):
        img = "playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)
        
    """
    * Gives the ability for the user to press the right arrow key
    * so they can rotate the ship based on the angle given.
    """    
    def rotate_right(self):
        self.angle -= SHIP_TURN_AMOUNT
    
    """
    * Gives the ability for the user to press the left arrow key
    * so they can rotate the ship based on the angle given.
    """
    def rotate_left(self):
        self.angle += SHIP_TURN_AMOUNT
          
    """
    * Lets the user slow down the ship and uses the down
    * arrow key to move backwards.
    """      
    def move_down(self): # Added function
        self.velocity.dx -= self.speed * math.cos(math.radians(self.angle)) 
        self.velocity.dy -= self.speed * math.sin(math.radians(self.angle))
    
    """
    * Lets the user increase there speed of the ship by
    * pressing the up arrow key. 
    """
    def increase_speed(self): # Move up
        self.velocity.dx += self.speed * math.cos(math.radians(self.angle)) 
        self.velocity.dy += self.speed * math.sin(math.radians(self.angle)) 
    

       
    
        
              