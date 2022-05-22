"""
 Program:
    Snake PyGame Playable Character
 Author:
    Aaron Jones
 Summary: 
    
                     
"""


import pygame
import random
from direction import Direction
from settings import *
# Named tuples assign a meaning to each position in a tuple and
# then they allow for a more readable and more self-documenting code.
from collections import namedtuple
pygame.mixer.init()
# Point object resembels a class.
# Named tuples can only take two arguments which is why the x and y
# are combined into one string variable.
Point = namedtuple('Point', 'x, y')  # lightweight version of a class
# named tuple has member variables 'x' and 'y' and can be acessed through Point.x or Point.y

"""
* This class will mimic the Pong game and create
* a snake that can move up and down the y axis
* within the set boundaries.
"""


class SnakeGame:

    def __init__(self):

        # inititalize display
        self.display = pygame.display.set_mode(
            (WIDTH, HEIGHT))  # tuple of (width, height)
        pygame.display.set_caption('Snake')
        # Used to control the speed of the game.
        self.clock = pygame.time.Clock()

        # initialize the game state
        # You could use a string here, but there is room for user typing error
        # self.direction = "right"
        self.direction = Direction.RIGHT

        # Taking a font from a file
        self.font = pygame.font.Font('arial.ttf', 25)
        # font = pygame.font.SysFont('arial', 25)  # Taking a font from the system
        # Using a font from a file creates a faster start up time.

        self.crash_sound = pygame.mixer.music.load('crash_sound.mp3')

        # Initialize the snake
        # Need to store coordinates inside of the display
        # We could use a list here with self.head = [w as the x-coordinate, has the y-coordinate]
        # although this format is proned to error.
        # self.head = [self.width, self.height]
        # Point gets x and y coordinates (half of width and half of height)
        self.head = Point(WIDTH/2, HEIGHT/2)

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
        x = random.randint(0, (WIDTH-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        # X has a random integer between zero and the width minus the block size.
        # '//' Then we want to have multiples of the block size so we divide it
        # by the block size and get an integer out of it.
        # '*'  Then its multiplied again by the block size.
        # This code ('//BLOCK_SIZE)*BLOCK_SIZE') will get a random precision
        # somewhere in the screen that are multiples of the block size.
        y = random.randint(0, (HEIGHT-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
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
        # This gets all the user event that happend insisde one play step.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # If the user pressed a key then we check if its an arrow key.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT  # Sets the direction to the left
                elif event.key == pygame.K_RIGHT:
                    # Sets the direction to the right.
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    # Sets the direction upward.
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    # Sets the direction downward.
                    self.direction = Direction.DOWN
                # Don't use an 'else' here because this would also be
                # the case for every other key the user pressed.

        # 2. Move the head of the snake
        self._move(self.direction)  # Update the head
        # Insert at the beginning with the new head into the list ('self.snake = []')
        # We don't use append here because we want to insert at the beginning.
        self.snake.insert(0, self.head)

        # 3. Check if game is over or if the user quit.
        game_over = False
        if self._is_collision():  # Another helper function
            game_over = True
            return game_over, self.score  # Here we immediately return

        # 4. Place new food if the snake hits the food or just move the snake.
        # This will finalize the move step (step #2).
        if self.head == self.food:  # If the snake catches the food then we increase the score.
            self.score += 1
            self._place_food()  # Helper function
        else:
            self.snake.pop()  # Removes the last element from the snake.

        # 5. Update the PyGame UI and the clock
        self._update_ui()
        self.clock.tick(SPEED)
        # 6. Return game over and score (needs to be added to the game loop).
        return game_over, self.score

    def _is_collision(self):
        # Check to see if the snake hits the boundary.
        if self.head.x > WIDTH - BLOCK_SIZE or self.head.x < 0 or self.head.y > HEIGHT - BLOCK_SIZE or self.head.y < 0:
            # The first two 'or' statements check to see if the snake hits the left or right boundary.
            # The second two 'or' statements check to see if the snake hits the top or bottom boundaries.
            # If the argument returns 'True' then the snake hit the boundary.
            pygame.mixer.music.play()
            return True
        # Check to see if the snake hits itself.
        # 'self.snake[1:]:' uses slicing; starts at position one
        # and goes all the way to the end because the first one
        # is the head itself. The head is always in the snake so
        # that is why we don't check the first position.
        # We only want to check all of the other positions.
        if self.head in self.snake[1:]:
            # If the argument returns 'True' then the snake hit itself.
            pygame.mixer.music.play()
            return True

        # If nothing happens then the snake didn't hit a wall or itself.
        return False

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
        text = self.font.render("Score: " + str(self.score), True, WHITE)
        # '[0, 0]' is in the upper left corner of the screen.
        self.display.blit(text, [0, 0])
        # Important - Without the code block below we won't see the changes.
        # Updating the full display surface to the screen.
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x  # Extract the x and the y coordinates
        y = self.head.y
        # Direction class uses the Enum values
        if direction == Direction.RIGHT:  # Examples of possible errors in code
            # direction == string literals: 'right', "RIGHT", "r".
            x += BLOCK_SIZE  # Increases the x by the block size.
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE  # Decreases the x by the block size.
        elif direction == Direction.DOWN:
            # Increase the y because it starts at zero in the top ('[0, 0 = y value at the top]').
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE  # Decreases the y by the block size.

        # Create a new head with a new Point that has new x and y values.
        self.head = Point(x, y)
