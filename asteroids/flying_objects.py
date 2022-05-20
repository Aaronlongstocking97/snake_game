"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will be the top of the hierarchy that other
    programs will derive from. Its base values will be passed
    through to other classes through polymorphism. 
                     
"""

from global_ import *
from point import Point
from velocity import Velocity
from abc import ABC
from abc import abstractmethod
import arcade

"""
* This class will set the architecture for other classes and there
* functionalities. 
"""
class FlyingObjects(ABC):

    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True
        self.angle = 0
    """
    * Passes in the values from the Point and Velocity classes
    * to give the objects movement. 
    """
    def advance(self):
      self.center.x += self.velocity.dx
      self.center.y += self.velocity.dy

    """
    * A decorated function that cannot be changed unless the abstract
    * methods or properties are overridden. 
    """
    @abstractmethod
    def draw(self):
        pass
   
