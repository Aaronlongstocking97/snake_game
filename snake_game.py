"""
 Program:
    Snake PyGame - A 2D Snake Game
 Author:
    Aaron Jones
 Summary: 
    This program controls the Snake game by mimicking the
    main function. It will activate multiples classes to
    simulate the games design and display to the user
    a window that can be interacted with.
                     
"""

import pygame
import random
# Enum is a set of symbolic names that are bond to unique values.
from enum import Enum
# Named tuples assign a meaning to each position in a tuple and
# then they allow for a more readable and more self-documenting code.
from collections import namedtuple

pygame.init()  # Needed to initialize all the Class modules ('__init__') correctly (Start)

font = pygame.font.Font('arial.ttf', 25)  # Taking a font from a file
# font = pygame.font.SysFont('arial', 25)  # Taking a font from the system
# Using a font from a file creates a faster start up time.


class Direction(Enum):
    # Upper case names are used when defining constants
    RIGHT = 1
    LEFT = 2
    UP = 3
    # Cannot have 'down' with lower case or as a 'string' or a number.
    DOWN = 4


# Point object resembels a class.
# Named tuples can only take two arguments which is why the x and y
# are combined into one string variable.
Point = namedtuple('Point', 'x, y')  # lightweight version of a class
# named tuple has member variables 'x' and 'y' and can be acessed through Point.x or Point.y


# PyGame rgb colors
WHITE = (255, 255, 255)  # Global Tuples
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)  # Brighter blue
BLACK = (0, 0, 0)

# Global constants
BLOCK_SIZE = 20
SPEED = 40


class SnakeGame:

    def __init__(self, width=640, height=480):

        self.width = width
        self.height = height

        # inititalize display
        self.display = pygame.display.set_mode(
            (self.width, self.height))  # tuple of (width, height)
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()  # Used to control the speed of the game

        # initialize the game state
        # You could use a string here, but there is room for user typing error
        # self.direction = "right"
        self.direction = Direction.RIGHT

        # Initialize the snake
        # Need to store coordinates inside of the display
        # We could use a list here with self.head = [w as the x-coordinate, h as the y-coordinate]
        # although this format is proned to error.
        # self.head = [self.width, self.height]
        # Point gets x and y coordinates (half of width and half of height)
        self.head = Point(self.width/2, self.height/2)

        # Create the snake
        # 'Point(self.head.x' Can only be used because it is a namedtuple.
        # 'Point(self.head.x-1' We won't use this because we want our snake
        # to be bigger than one pixel.
        # Store three coordinates: head,
        # first Point: x-coordinate but placed to the left with the same y-coordinate,
        # second Point: x-coordinate shifted two blocks to the left with
        # the same y-coordinate.
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0  # Keep track of the score
        self.food = None
        # We want to randomaly place the food with this helper function.
        self._place_food()  # This helper function is a function that performs
        # part of the computation of another funciton following the
        # DRY (don't repeat yourself) concept.

        def _place_food(self):  # Helper function
            # Creating a random coordinate inside x and y dimensions
            x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            # X has a random integer between zero and the width minus the block size.
            # '//' Then we want to have multiples of the block size so we divide it
            # by the block size and get an integer out of it.
            # '*'  Then its multiplied again by the block size.
            # This code ('//BLOCK_SIZE)*BLOCK_SIZE') will get a random precision
            # somewhere in the screen that are multiples of the block size.
            y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
            # After both random variables ('x,y')are created it will try test the
            # food variable ('self.food') and if it is not inside of the
            # snake ('if self.food in self.snake') then it will pass.
            self.food = Point(x, y)
            if self.food in self.snake:  # Keeps the food from being placed inside the snake.
                # If the food is in the list then we do the same thing again and call
                # this function again recursively.
                self._place_food()

        # place the food and the inital snake

        def play_step(self):
            # 1. Collect the user input and see what key the user pressed.

            # 2. Move the snake

            # 3. Check if game is over or if the user quit.
            game_over = False
            # 4. Place new food if the snake hits the food or just move the snake.
            # This will finalize the move step (step #2).

            # 5. Update the PyGame UI and the clock
            self._update_ui()
            self.clock.tick(SPEED)
            # 6. Return game over and score (needs to be added to the game loop).
            return game_over, self.score

        def _update_ui(self):
            # Order here is important
            self.display.fill(BLACK)  # First

            # Draw the snake
            for pt in self.snake:  # Iterate over all the points
                pygame.draw.rect(self.display, BLUE1, pygame.Rect(
                    pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))  # pt.x and pt.y is accessible
                # because of the namedtuple. Block size in width and height times two.
                pygame.draw.rect(self.display, BLUE2,
                                 pygame.Rect(pt.x+4, pt.y+4, 12, 12))
                # Drawing a slightly smaller rectangle thats placed to the right

            # Draw the food
            pygame.draw.rect(self.display, RED, pygame.Rect(
                self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))  # Same block size as the snake

            # Draw the score in the upper left corner of the  screen.
            text = font.render("Score: " + str(self.score), True, WHITE)
            # '[0, 0]' is in the upper left corner of the screen.
            self.display.blit(text, [0, 0])
            # Important - Without the code block below we won't see the changes.
            # Updating the full display surface to the screen.
            pygame.display.flip()


if __name__ == '__main__':
    game = SnakeGame()

    # game Loop
    while True:

        game_over, score = game.play_step()

        # break if game over
        if game_over == True:
            break  # Exist the while True Loop

        print('Final Score', score)

    pygame.quit()  # (Stop)
