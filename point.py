"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary:
    This Class will set the inital state values for
    both x and y axis as well as set each point to
    a floating point value. It will also be
    passed through multiple class' with a "Has - A"
    relationship and gives the default values as
    listed below. Uses encapsulation so that the objects
    listed are set values that cannot be changed. Used to
    wrap the objects around the screen. 
 
"""

"""
* This class will set the intial values that can be
* passed into other classes. These values will be
* set through encapsulation using the SETTER decorator
* function name.
"""

from global_ import *

class Point:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
    """
    * A decoraded function that checks the value limits
    * listed in the initalizer.
    """
    @property
    def x(self):
        return self._x
    
    """
    * Sets the x-axis so the objects will not leave
    * the screen. Once the value is set it cannot be
    * changed and is considered private.
    """
    @x.setter
    def x(self, x):
        if x >= SCREEN_WIDTH:
            self._x = 0
        elif x < 0:
            self._x = SCREEN_WIDTH
        else:
            self._x = x
    
    """
    * A decoraded function that checks the value limits
    * listed in the initalizer.
    """
    @property
    def y(self):
        return self._y
    
    """
    * Sets the x-axis so the objects will not leave
    * the screen. Once the value is set it cannot be
    * changed and is considered private.
    """
    @y.setter
    def y(self, y):
        if y >= SCREEN_HEIGHT:
            self._y = 0
        elif y < 0:
            self._y = SCREEN_HEIGHT
        else:
            self._y = y
    
    
    
    