"""
 Program:
    Snake PyGame Direction
 Author:
    Aaron Jones
 Summary: 
    This class will set the intial state values
    for both x and y velocities. Giving them a
    floating point value to emphasize that they
    will be part of a random.uniform system in
    a seperate class.
    
"""

import enum


class Direction(enum.Enum):
    # Upper case names are used when defining constants
    RIGHT = 1
    LEFT = 2
    UP = 3
    # Cannot have 'down' with lower case or as a 'string' or a number.
    DOWN = 4
