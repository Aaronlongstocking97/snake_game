"""
 Program:
    Snake PyGame Direction
 Author:
    Aaron Jones
 Summary: 
    This class will set the control the movement
    of the snake. The Directions class uses the enum 
    to help showcase data that represents a finite set 
    of states such as days of the week or months of the year.    
"""
# Enum is a set of symbolic names that are bond to unique values.
import enum


class Direction(enum.Enum):
    # Upper case names are used when defining constants
    RIGHT = 1
    LEFT = 2
    UP = 3
    # Cannot have 'down' with lower case or as a 'string' or a number.
    DOWN = 4
