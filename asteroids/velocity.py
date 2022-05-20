"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    This class will set the intial state values
    for both x and y velocities. It will also be
    passed through multiple class' with a "Has - A"
    relationship and gives the default values as
    listed below.
    
"""

"""
* This class will set the intial values that can be
* passed into other classes.
"""
class Velocity:

    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0
