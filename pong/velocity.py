"""
 Program:
    Pong Arcade Velocity
 Author:
    Aaron Jones
 Summary: 
    This class will set the intial state values
    for both x and y velocities. Giving them a
    floating point value to emphasize that they
    will be part of a random.uniform system in
    a seperate class.
    
"""


class Velocity:
    """
    * Sets the inital state values
    * for the Velocity class.
    """

    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0
