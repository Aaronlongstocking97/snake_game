"""
 Program:
    Snake PyGame Application Window & Game Board Constants
 Author:
    Aaron Jones
 Summary: 
    These are global constants that will be used
    throughout the game. Each constant is set
    to a value that is in the parementers of
    the game box and will effect each class
    based on the implementation of the global.
                     
"""

import pygame

# Application window. Size in pixels.
WIDTH = 640
HEIGHT = 480

# # Game grid system. Cell (one grid square) size in pixels.
# CELL = 16
# COLUMNS = int(SCREEN_WIDTH / CELL)
# ROWS = int(SCREEN_HEIGHT / CELL)

# # Padding between the game board & window borders. Units in "cells".
# PADDING = {'left': 1, 'right': 1, 'top': 6, 'bottom': 1}

# # Game board edges.
# BOARD_LEFT = PADDING['left'] + 1
# BOARD_RIGHT = COLUMNS - (PADDING['right'])
# BOARD_TOP = ROWS - (PADDING['top'])
# BOARD_BOTTOM = PADDING['bottom'] + 1

# FOOD_WIDTH = 10
# FOOD_HEIGHT = 10

# SNAKE_WIDTH = 10
# SNAKE_HEIGHT = 10
# MOVE_AMOUNT = 5

# SCORE_HIT = 1
# SCORE_MISS = 5

# PyGame rgb colors
WHITE = (255, 255, 255)  # Global Tuples
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)  # Brighter blue
BLACK = (0, 0, 0)

# Global constants
BLOCK_SIZE = 20
SPEED = 20

crash_sound = pygame.mixer.Sound('crash_sound.wav')
