"""
 Program:
    Snake PyGame - A 2D Snake Game
 Author:
    Aaron Jones
 Summary: 
    This program controls the Snake game by using the
    main function. It will activate the snake class to
    simulate the games design and display to the user
    a window that can be interacted with.
                     
"""

import pygame
from snake import SnakeGame


def main():

    # Needed to initialize all the
    # Class modules ('__init__') correctly (Start)
    pygame.init()
    pygame.mixer.init()

    game = SnakeGame()

    # game Loop
    while True:

        game_over, score = game.play_step()

        # break if game over
        if game_over == True:
            # Added Sound effects
            crash = pygame.mixer.Sound("crashed.wav")
            pygame.mixer.Sound.play(crash)
            break  # Exist the while True Loop

    print('Final Score', score)

    pygame.quit()  # (Stop)


if __name__ == '__main__':
    main()
