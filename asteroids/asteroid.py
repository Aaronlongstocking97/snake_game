"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This program will be the top of a derived hierarchy, but will
    still Inherit the values from the FlyingObjects ABC. This class
    will also demonstrate forms of polymorphism through unique child
    classes that will be originated from this ABC.
                     
"""

import random
from global_ import *
from flying_objects import FlyingObjects
from abc import ABC
from abc import abstractmethod

"""
* This class will be the architecture for its child classes
* by establishing multiple abstract methods by acting as
* the parent class. It will also demonstrate the use of
* inheritance from objects in the FlyingObjects parent class.
"""
class Asteroid(FlyingObjects, ABC):

    def __init__(self):
        super().__init__()
        self.velocity.dx = 1.5
        self.velocity.dy = 1.5
        self.radius = 0
        self.angle = 0
        self.rotation = 0

    """
    * A decorated function that cannot be changed unless the abstract
    * methods or properties are overridden. 
    """
    @abstractmethod
    def draw(self):
        pass

    """
    * A decorated function that cannot be changed unless the abstract
    * methods or properties are overridden. 
    """
    
    @abstractmethod
    def hit(self):
        pass

        
        
        
